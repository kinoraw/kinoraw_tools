# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

bl_info = {
    "name": "Kinoraw Tools",
    "author": "Carlos Padial, Ferhoyo, Turi Scandurra",
    "version": (0, 1),
    "blender": (2, 72, 0),
    "category": "Sequencer",
    "location": "Sequencer",
    "description": "Collection of extra operators to manipulate VSE strips",
    "wiki_url": "http://wiki.blender.org/index.php/Extensions:2.6/Py/"
        "Scripts/Sequencer/Extra_Sequencer_Actions",
    "tracker_url": "https://developer.blender.org/T32532",
    "support": "COMMUNITY"}


if "bpy" in locals():
    import imp
    imp.reload(jumptocut)
    imp.reload(operators_extra_actions)
    imp.reload(audio_tools)
    imp.reload(proxy_tools)
    imp.reload(recursive_loader)
    imp.reload(eco)
    imp.reload(random_editor)
    imp.reload(ui)
else:
    from . import jumptocut
    from . import operators_extra_actions
    from . import audio_tools
    from . import proxy_tools
    from . import recursive_loader
    from . import eco
    from . import random_editor
    from . import ui

import bpy
import os.path
from bpy.types import Menu
from bpy.types import Header

from bpy.props import IntProperty, StringProperty, BoolProperty, EnumProperty


class KinorawToolsAddon(bpy.types.AddonPreferences):
    bl_idname = "kinoraw_tools"
    bl_option = {'REGISTER'}

    use_extra_actions_panel = BoolProperty(
    name = 'extra actions panel',
    default = True)

    mini_extra_actions = BoolProperty(
    name = 'enable mini UI',
    default = True)

    use_exif_panel = BoolProperty(
    name = 'exif info panel',
    default = True)

    # jump to cut

    use_jumptocut = BoolProperty(
    name = 'jumptocut panel',
    default = True)

    use_io_tools = BoolProperty(
    name = 'enable in and out tools in jumptocut panel',
    default = True)

    # Proxy Tools

    use_proxy_tools = BoolProperty(
    name = 'proxy tools panel',
    default = True)

    proxy_dir = StringProperty(
    name = 'Proxy Custom Directory',
    default = "//proxies/")

    proxy_scripts_path = StringProperty(
    name = 'directory to store proxy scripts',
    default = "//proxy_scripts/")

    proxy_scripts = BoolProperty(
    name = 'generate ffmpeg scritps',
    default = False)

    ffmpeg_command = StringProperty(
    name = 'command to generate proxy',
    default = '''ffmpeg -i {} -vcodec mjpeg -q:v 10 -s {}x{} -an -y {}''')

    use_internal_proxy = BoolProperty(
    name = 'use internal blender proxy system',
    default = True)

    use_bi_custom_directory = BoolProperty(
    name = 'Proxy Custom Directory',
    default = True)

    quality = IntProperty(
        name = 'Quality',
        default = 90,
        min = 0, max = 32767)

    tc_list = [  ( "NONE", "No TC in use","" ), ( "RECORD_RUN", "Record Run", "" ),
                    ( "FREE_RUN", "Free Run", "" ), ("FREE_RUN_REC_DATE", "Free Run (rec date)", "" ),
                    ( "RECORD_RUN_NO_GAPS", "Record Run No Gaps", "" )]

    timecode = EnumProperty(
        name = "Settings Type", 
        items = tc_list, 
        default="NONE",
        description = "timecode" ) 

    # Audio Tools

    use_audio_tools = BoolProperty(
    name='audio tools panel',
    default=True)
    
    audio_dir = StringProperty(
    name='path to store extracted audio',
    default="//audio/")

    audio_scripts_path = StringProperty(
    name='path to store audio scripts',
    default="//audio_scripts/")

    audio_scripts = BoolProperty(
    name='generate ffmpeg scritps',
    default=False)

    # external links

    audio_use_external_links = BoolProperty(
        name='use external audio linked to movie strips',
        default=False)

    audio_external_filename = StringProperty(
    name='file to store info about linked audio',
    default="//external_audio_sync_info.txt")

    # eco

    use_eco_tools = BoolProperty(
    name='eco tools panel',
    default=True)

    eco_value = IntProperty(
        name = 'number of echoes',
        default = 5,
        min = 1, max = 25)

    eco_offset = IntProperty(
        name = 'Echo Offset',
        default = 1,
        min = -25000, max = 25000)

    eco_use_add_blend_mode = BoolProperty(
        name = 'use_add_blend_mode',
        default = False)

    # random editor

    use_random_editor = BoolProperty(
    name='random editor panel',
    default=True)

    random_frames = IntProperty(
            name='frames',
            default=1,
            min = 1, max = 1000)
            
    random_selected_scene = StringProperty(
        name = 'selected_scene',
        default = 'pessics3.limpio')
        
    random_use_marker_subsets = BoolProperty(
        name = 'use_marker_subsets',
        default = True)
        
    random_number_of_subsets = IntProperty(
        name = 'number_of_subsets',
        default = 3,
        min = 1, max = 5)

    def draw(self, context):

        layout = self.layout
        layout.prop(self, "use_exif_panel")

        layout = self.layout
        layout.prop(self, "use_eco_tools")

        layout = self.layout
        layout.prop(self, "use_random_editor")

        layout = self.layout
        layout.prop(self, "use_jumptocut")

        # PROXY
        layout = self.layout
        layout.prop(self, "use_proxy_tools")

        # AUDIO
        layout = self.layout
        layout.prop(self, "use_audio_tools")

        # EXTRA ACTIONS
        layout = self.layout
        layout.prop(self, "use_extra_actions_panel")


# Registration
def register():
    bpy.utils.register_module(__name__)

    # Append menu entries
    bpy.types.SEQUENCER_MT_add.prepend(ui.sequencer_add_menu_func)
    bpy.types.SEQUENCER_MT_select.prepend(ui.sequencer_select_menu_func)
    bpy.types.SEQUENCER_MT_strip.prepend(ui.sequencer_strip_menu_func)
    bpy.types.SEQUENCER_HT_header.append(ui.sequencer_header_func)
    bpy.types.CLIP_HT_header.append(ui.clip_header_func)
    bpy.types.CLIP_MT_clip.prepend(ui.clip_clip_menu_func)
    bpy.types.TIME_MT_frame.prepend(ui.time_frame_menu_func)
    bpy.types.TIME_HT_header.append(ui.time_header_func)

    # Add keyboard shortcut configuration
    kc = bpy.context.window_manager.keyconfigs.addon
    km = kc.keymaps.new(name='Frames')

    # jump 1 second
    kmi = km.keymap_items.new('screenextra.frame_skip',
    'RIGHT_ARROW', 'PRESS', ctrl=True, shift=True)
    kmi.properties.back = False
    kmi = km.keymap_items.new('screenextra.frame_skip',
    'LEFT_ARROW', 'PRESS', ctrl=True, shift=True)
    kmi.properties.back = True

    
    # jumptocut shortcuts
    kmi = km.keymap_items.new('sequencerextra.jumptocut',
    'Q', 'PRESS', ctrl=False, shift=False)
    kmi.properties.next = False
    kmi = km.keymap_items.new('sequencerextra.jumptocut',
    'W', 'PRESS', ctrl=False, shift=False)
    kmi.properties.next = True

     # in and out
    kmi = km.keymap_items.new("sequencerextra.sourcein",
    'I', 'PRESS', ctrl=True, shift=True)
    kmi = km.keymap_items.new("sequencerextra.sourceout",
    'O', 'PRESS', ctrl=True, shift=True)

    #markers
    kc = bpy.context.window_manager.keyconfigs.active
    km = kc.keymaps.new(name='Screen')
    kmi = km.keymap_items.new("screen.marker_jump",
    'Q', 'PRESS', ctrl=False, shift=True)
    kmi.properties.next=False
    kmi = km.keymap_items.new("screen.marker_jump",
    'W', 'PRESS', ctrl=False, shift=True)
    kmi.properties.next=True


def unregister():
    bpy.utils.unregister_module(__name__)

    #  Remove menu entries
    bpy.types.SEQUENCER_MT_add.remove(ui.sequencer_add_menu_func)
    bpy.types.SEQUENCER_MT_select.remove(ui.sequencer_select_menu_func)
    bpy.types.SEQUENCER_MT_strip.remove(ui.sequencer_strip_menu_func)
    bpy.types.SEQUENCER_HT_header.remove(ui.sequencer_header_func)
    bpy.types.CLIP_HT_header.remove(ui.clip_header_func)
    bpy.types.CLIP_MT_clip.remove(ui.clip_clip_menu_func)
    bpy.types.TIME_MT_frame.remove(ui.time_frame_menu_func)
    bpy.types.TIME_HT_header.remove(ui.time_header_func)

    #  Remove keyboard shortcut configuration
    kc = bpy.context.window_manager.keyconfigs.addon
    km = kc.keymaps['Frames']
    km.keymap_items.remove(km.keymap_items['screenextra.frame_skip'])
    km.keymap_items.remove(km.keymap_items['screenextra.frame_skip'])

    
    km.keymap_items.remove(km.keymap_items['sequencerextra.jumptocut'])
    km.keymap_items.remove(km.keymap_items['sequencerextra.jumptocut'])


    km.keymap_items.remove(km.keymap_items['sequencerextra.sourcein'])
    km.keymap_items.remove(km.keymap_items['sequencerextra.sourceout'])


    kc = bpy.context.window_manager.keyconfigs.active
    km = kc.keymaps['Screen']
    km.keymap_items.remove(km.keymap_items['screen.marker_jump'])
    km.keymap_items.remove(km.keymap_items['screen.marker_jump'])
    

if __name__ == '__main__':
    register()
