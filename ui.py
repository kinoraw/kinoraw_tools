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

import bpy

from . import functions



# UI
class SEQUENCER_EXTRA_MT_input(bpy.types.Menu):
    bl_label = "Input"

    def draw(self, context):
        self.layout.operator_context = 'INVOKE_REGION_WIN'
        self.layout.operator('sequencerextra.striprename',
        text='File Name to Strip Name', icon='PLUGIN')
        self.layout.operator('sequencerextra.editexternally',
        text='Open with External Editor', icon='PLUGIN')
        self.layout.operator('sequencerextra.edit',
        text='Open with Editor', icon='PLUGIN')
        self.layout.operator('sequencerextra.createmovieclip',
        text='Create Movieclip strip', icon='PLUGIN')


def sequencer_add_menu_func(self, context):
    # menu to show recursive load operators
    self.layout.operator('sequencerextra.recursiveload', 
    text='recursive load from browser', icon='PLUGIN')
    self.layout.separator()


def sequencer_select_menu_func(self, context):
    self.layout.operator_menu_enum('sequencerextra.select_all_by_type',
    'type', text='All by Type', icon='PLUGIN')
    self.layout.separator()
    self.layout.operator('sequencerextra.selectcurrentframe',
    text='Before Current Frame', icon='PLUGIN').mode = 'BEFORE'
    self.layout.operator('sequencerextra.selectcurrentframe',
    text='After Current Frame', icon='PLUGIN').mode = 'AFTER'
    self.layout.operator('sequencerextra.selectcurrentframe',
    text='On Current Frame', icon='PLUGIN').mode = 'ON'
    self.layout.separator()
    self.layout.operator('sequencerextra.selectsamechannel',
    text='Same Channel', icon='PLUGIN')


def sequencer_strip_menu_func(self, context):
    self.layout.operator('sequencerextra.extendtofill',
    text='Extend to Fill', icon='PLUGIN')
    self.layout.operator_menu_enum('sequencerextra.fadeinout',
    'mode', text='Fade', icon='PLUGIN')
    self.layout.operator_menu_enum('sequencerextra.copyproperties',
    'prop', icon='PLUGIN')
    
    self.layout.operator('sequencerextra.insert',
    text='Insert (Single Channel)', icon='PLUGIN').singlechannel = True
    self.layout.operator('sequencerextra.insert',
    text='Insert', icon='PLUGIN').singlechannel = False
    self.layout.operator('sequencerextra.ripplecut',
    text='Ripple Cut', icon='PLUGIN')
    self.layout.operator('sequencerextra.rippledelete',
    text='Ripple Delete', icon='PLUGIN')
    self.layout.separator()


def sequencer_header_func(self, context):
    self.layout.menu("SEQUENCER_EXTRA_MT_input")
    """if context.space_data.view_type in ('PREVIEW', 'SEQUENCER_PREVIEW'):
        self.layout.operator('sequencerextra.jogshuttle',
        text='Jog/Shuttle', icon='NDOF_TURN')
    if context.space_data.view_type in ('SEQUENCER', 'SEQUENCER_PREVIEW'):
        self.layout.operator('sequencerextra.navigateup',
        text='Navigate Up', icon='FILE_PARENT')
    if context.space_data.view_type in ('SEQUENCER', 'SEQUENCER_PREVIEW'):
        self.layout.operator('sequencerextra.placefromfilebrowser',
        text='File Place', icon='TRIA_DOWN').insert = False
    if context.space_data.view_type in ('SEQUENCER', 'SEQUENCER_PREVIEW'):
        self.layout.operator('sequencerextra.placefromfilebrowser',
        text='File Insert', icon='TRIA_RIGHT').insert = True"""


def time_frame_menu_func(self, context):
    self.layout.operator('timeextra.trimtimelinetoselection',
    text='Trim to Selection', icon='PLUGIN')
    self.layout.operator('timeextra.trimtimeline',
    text='Trim to Timeline Content', icon='PLUGIN')
    self.layout.separator()
    self.layout.operator('screenextra.frame_skip',
    text='Skip Forward One Second', icon='PLUGIN').back = False
    self.layout.operator('screenextra.frame_skip',
    text='Skip Back One Second', icon='PLUGIN').back = True
    self.layout.separator()


def time_header_func(self, context):
    self.layout.operator('sequencerextra.jogshuttle',
    text='Jog/Shuttle', icon='NDOF_TURN')


def clip_header_func(self, context):
    self.layout.operator('sequencerextra.jogshuttle',
    text='Jog/Shuttle', icon='NDOF_TURN')


def clip_clip_menu_func(self, context):
    self.layout.operator('clipextra.openactivestrip',
    text='Open Active Strip', icon='PLUGIN')
    self.layout.operator('clipextra.openfromfilebrowser',
    text='Open from File Browser', icon='PLUGIN')
    self.layout.separator()


class ExtraActions(bpy.types.Panel):
    bl_space_type = "SEQUENCE_EDITOR"
    bl_region_type = "UI"
    bl_label = "Extra Actions"

    @classmethod
    def poll(self, context):
        if context.space_data.view_type in {'SEQUENCER', 'SEQUENCER_PREVIEW'}:
            strip = functions.act_strip(context)
            scn = context.scene
            preferences = context.user_preferences
            prefs = preferences.addons[__package__].preferences
            if scn and scn.sequence_editor:
                if prefs.use_extra_actions_panel and strip != None:
                    return True
        else:
            return False

    def draw_header(self, context):
        layout = self.layout
        layout.label(text="", icon="RENDER_ANIMATION")

    def draw(self, context):
        scn = context.scene
        strip = scn.sequence_editor.active_strip

        preferences = context.user_preferences
        prefs = preferences.addons[__package__].preferences

        layout = self.layout
        if prefs.mini_extra_actions:
            row=layout.row(align=True)
            row.operator('screenextra.frame_skip',
            text="", icon='TRIA_LEFT').back = True
            row.operator('screenextra.frame_skip',
            text="", icon='TRIA_RIGHT').back = False
            row.label(str(context.scene.render.fps)+ " frames = 1 sec")
            row.prop(prefs, "mini_extra_actions", text="mini UI")

            row=layout.row(align=True)
            row.operator('sequencerextra.jogshuttle',
                text='', icon='NDOF_TURN')
            row.operator('sequencerextra.navigateup',
                text='', icon='FILE_PARENT')
            row.operator('sequencerextra.extendtofill',
            text='', icon='STYLUS_PRESSURE')
            row.operator('sequencerextra.placefromfilebrowser',
                text='', icon='TRIA_DOWN').insert = False            
            row.operator('sequencerextra.placefromfilebrowser',
                text='', icon='TRIA_RIGHT').insert = True
            row.operator('sequencer.slip',
                text='', icon='MOD_SHRINKWRAP')
            row.operator_menu_enum('sequencerextra.fadeinout',
            'mode', text='fade', icon='MOD_ARRAY')
            row.operator_menu_enum('sequencerextra.copyproperties',
            'prop', text='copy',icon='SCRIPT')

        else:
            row=layout.row(align=True)
            row.operator('screenextra.frame_skip',
            text="", icon='TRIA_LEFT').back = True
            row.operator('screenextra.frame_skip',
            text="", icon='TRIA_RIGHT').back = False
            row.label(str(context.scene.render.fps)+ " frames = 1 sec")

            
            row.operator('sequencerextra.jogshuttle',
                text='Jog/Shuttle', icon='NDOF_TURN')

            
            layout = self.layout

            row=layout.row(align=True)

            row.operator('sequencerextra.navigateup',
                text='Navigate Up', icon='FILE_PARENT')

            row.operator('sequencerextra.extendtofill',
            text='Extend to Fill', icon='STYLUS_PRESSURE')

            row=layout.row(align=True)
            
            row.operator('sequencerextra.placefromfilebrowser',
                text='File Place', icon='TRIA_DOWN').insert = False
            
            row.operator('sequencerextra.placefromfilebrowser',
                text='File Insert', icon='TRIA_RIGHT').insert = True

            row.operator('sequencer.slip',
                text='Slip', icon='MOD_SHRINKWRAP')

            layout = self.layout

            row=layout.row(align=True)
            row.operator_menu_enum('sequencerextra.fadeinout',
            'mode', text='Fade', icon='MOD_ARRAY')
            row.operator_menu_enum('sequencerextra.copyproperties',
            'prop', icon='SCRIPT')
            

        if prefs.mini_extra_actions == False:
            layout = self.layout
            layout.prop(prefs, "mini_extra_actions")

        layout = self.layout

        box = layout.box()
        
        row=box.row(align=True)
        row.label(text="Active Strip:")
        row.prop(strip, "name", text="")

        row = box.split(percentage=0.3)
        row.prop(strip, "type", text="")
        if strip.type not in {'SOUND'}:
            # draw a filename if we have one
            if strip.type == 'IMAGE':
                row.prop(strip, "directory", text="")

                # Current element for the filename
                elem = strip.strip_elem_from_frame(context.scene.frame_current)
                if elem:
                    split = row.split(percentage=0.2)
                    split.label(text="File:")
                    split.prop(elem, "filename", text="")  # strip.elements[0] could be a fallback
                layout.operator("sequencer.change_path")

            elif strip.type == 'MOVIE':
                row.prop(strip, "filepath", text="")

            row = box.row(align=True)
            split = box.split(percentage=0.3)
            split.label(text="Blend:")
            split.prop(strip, "blend_type", text="")
            split.prop(strip, "use_float", text="Float")


            sub = row.row(align=True)
            sub.active = (not strip.mute)
            sub.prop(strip, "blend_alpha", text="Opacity", slider=True)
            row.prop(strip, "mute", toggle=True, icon_only=True)
            row.prop(strip, "lock", toggle=True, icon_only=True)

            col = box.row(align=True)
            col.prop(strip, "color_saturation", text="Saturation")
            col.prop(strip, "color_multiply", text="Multiply")
        #sound type
        else:
            row.prop(strip, "filepath", text="")
            row = box.row(align=True)
            row.prop(strip, "volume")
            row.prop(strip, "mute", toggle=True, icon_only=True)
            row.prop(strip, "lock", toggle=True, icon_only=True)
            
            sound = strip.sound
            if sound is not None:
                row = box.row()
                if sound.packed_file:
                    row.operator("sound.unpack", icon='PACKAGE', text="Unpack")
                else:
                    row.operator("sound.pack", icon='UGLYPACKAGE', text="Pack")

                row.prop(sound, "use_memory_cache")

            row.prop(strip, "show_waveform")
            
            row = box.row()
            row.prop(strip, "pitch")
            row.prop(strip, "pan")

        

        


        
        

        









