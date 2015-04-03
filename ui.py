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

def sequencer_header_func(self, context):
    self.layout.menu("SEQUENCER_EXTRA_MT_input")

def sequencer_add_menu_func(self, context):
    self.layout.operator('sequencerextra.placefromfilebrowser', 
    text='place from file browser', icon='PLUGIN').insert = False
    self.layout.operator('sequencerextra.placefromfilebrowser', 
    text='insert from file browser', icon='PLUGIN').insert = True
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



        

class JumptoCut(bpy.types.Panel):
    bl_space_type = "SEQUENCE_EDITOR"
    bl_region_type = "UI"
    bl_label = "JumptoCut"

    COMPAT_ENGINES = {'BLENDER_RENDER'}
    
    _frame_rate_args_prev = None
    _preset_class = None

    @staticmethod
    def _draw_framerate_label(*args):
        # avoids re-creating text string each draw
        if JumptoCut._frame_rate_args_prev == args:
            return JumptoCut._frame_rate_ret

        fps, fps_base, preset_label = args

        if fps_base == 1.0:
            fps_rate = round(fps)
        else:
            fps_rate = round(fps / fps_base, 2)

        # TODO: Change the following to iterate over existing presets
        custom_framerate = (fps_rate not in {23.98, 24, 25, 29.97, 30, 50, 59.94, 60})

        if custom_framerate is True:
            fps_label_text = "Custom (%r fps)" % fps_rate
            show_framerate = True
        else:
            fps_label_text = "%r fps" % fps_rate
            show_framerate = (preset_label == "Custom")

        JumptoCut._frame_rate_args_prev = args
        JumptoCut._frame_rate_ret = args = (fps_label_text, show_framerate)
        return args

    @staticmethod
    def draw_framerate(sub, rd):
        if JumptoCut._preset_class is None:
            JumptoCut._preset_class = bpy.types.RENDER_MT_framerate_presets

        args = rd.fps, rd.fps_base, JumptoCut._preset_class.bl_label
        fps_label_text, show_framerate = JumptoCut._draw_framerate_label(*args)

        sub.menu("RENDER_MT_framerate_presets", text=fps_label_text)

        if show_framerate:
            sub.prop(rd, "fps")
            sub.prop(rd, "fps_base", text="/")

    @classmethod
    def poll(self, context):
        if context.space_data.view_type in {'SEQUENCER', 'SEQUENCER_PREVIEW'}:
            strip = functions.act_strip(context)
            scn = context.scene
            preferences = context.user_preferences
            prefs = preferences.addons[__package__].preferences
            if scn and scn.sequence_editor:
                if prefs.use_jumptocut:
                    return True
        else:
            return False

    def draw_header(self, context):
        layout = self.layout
        layout.label(text="", icon="RENDER_ANIMATION")

    def draw(self, context):
        scn = context.scene
        strip = functions.act_strip(context)
            
        preferences = context.user_preferences
        prefs = preferences.addons[__package__].preferences
        
        layout = self.layout
        
        layout = layout.box()

        row=layout.row(align=True)
        split=row.split()
        colR1 = split.column()
        row1=colR1.row(align=True)
        row1.operator("sequencer.strip_jump", icon="PLAY_REVERSE", text="cut").next=False
        row1.operator("sequencer.strip_jump", icon='PLAY', text="cut").next=True
        colR2 = split.column()
        row2=colR2.row(align=True)
        row2.operator("screen.marker_jump", icon="TRIA_LEFT", text="marker").next=False
        row2.operator("screen.marker_jump", icon='TRIA_RIGHT', text="marker").next=True

        row=layout.row(align=True)
        row.operator("sequencerextra.setstartend", icon="PREVIEW_RANGE", text="IN/OUT")
        row.operator('timeextra.trimtimelinetoselection', text='Selection', icon='PREVIEW_RANGE')
        row.operator('timeextra.trimtimeline', text='All', icon='PREVIEW_RANGE')

        row=layout.row(align=True)
        row.label("Snap:")    
        #row=layout.row(align=True)
        row.operator('sequencerextra.extrasnap', text='left', icon='SNAP_ON').align=0
        row.operator('sequencerextra.extrasnap', text='center', icon='SNAP_ON').align=1
        row.operator('sequencerextra.extrasnap', text='right', icon='SNAP_ON').align=2

        row=layout.row(align=True)
        row.label("Handlers:")
        #row=layout.row(align=True)
        row.operator('sequencerextra.extrahandles', text='left', icon='TRIA_LEFT').side=0
        row.operator('sequencerextra.extrahandles', text='both', icon='PMARKER').side=1
        row.operator('sequencerextra.extrahandles', text='right', icon='TRIA_RIGHT').side=2

        row=layout.row()
        row=layout.row(align=True)
        split = row.split(percentage=0.99)
        colR2 = split.column()
        row1 = colR2.row(align=True)
        row1.operator("sequencerextra.metacopy", icon="COPYDOWN", text="meta-copy")
        row1.operator("sequencerextra.metapaste", icon='PASTEDOWN', text="paste-snap")
        
        split = row.split(percentage=0.99)
        colR3 = split.column()
        colR3.operator('sequencerextra.meta_separate_trim', text='unMeta & Trim', icon='ALIGN')
        
        row=layout.row(align=True)
        row.prop(prefs, "use_io_tools", text="In/Out tools:")
        
        if prefs.use_io_tools:
            row=layout.row(align=True)
            split=row.split(percentage=0.7)
            colR1 = split.column()
            row1=colR1.row(align=True)
            row1.operator("sequencerextra.sourcein", icon="MARKER_HLT", text="set IN")
            row1.operator("sequencerextra.sourceout", icon='MARKER_HLT', text="set OUT")
            colR3 = split.column()
            colR3.operator("sequencerextra.setinout", icon="ARROW_LEFTRIGHT", text="selected")
            
            row_markers=layout.row(align=True)
            split=row_markers.split(percentage=0.7)
            colR1 = split.column()
            row1=colR1.row(align=True)
            if scn.kr_auto_markers == False:
                row1.prop(scn, "kr_auto_markers", text="auto markers")
            else:
                row1.prop(scn, "kr_auto_markers", text="")
                row1.prop(scn, "kr_in_marker")
                row1.prop(scn, "kr_out_marker")
                row1.active = scn.kr_auto_markers
            colR3 = split.column()
            colR3.operator("sequencerextra.triminout", icon="FULLSCREEN_EXIT", text="trim",emboss=True)

        # draw del extra actions
        layout = self.layout

        layout = layout.box()
        
        rd = scn.render
        screen = context.screen
        row = layout.row(align=True)
        row.operator("screen.frame_jump", text="", icon='REW').end = False
        row.operator("screen.keyframe_jump", text="", icon='PREV_KEYFRAME').next = False
        if not screen.is_animation_playing:
            # if using JACK and A/V sync:
            #   hide the play-reversed button
            #   since JACK transport doesn't support reversed playback
            if scn.sync_mode == 'AUDIO_SYNC' and context.user_preferences.system.audio_device == 'JACK':
                sub = row.row(align=True)
                sub.scale_x = 2.0
                sub.operator("screen.animation_play", text="", icon='PLAY')
            else:
                row.operator("screen.animation_play", text="", icon='PLAY_REVERSE').reverse = True
                row.operator("screen.animation_play", text="", icon='PLAY')
        else:
            sub = row.row(align=True)
            sub.scale_x = 2.0
            sub.operator("screen.animation_play", text="", icon='PAUSE')
        row.operator("screen.keyframe_jump", text="", icon='NEXT_KEYFRAME').next = True
        row.operator("screen.frame_jump", text="", icon='FF').end = True
        
        row.separator()
        row.prop(scn, "sync_mode", text="")
        row.separator()
        self.draw_framerate(row, rd)
        
        row=layout.row(align=True)
        row.operator('screenextra.frame_skip',
        text="", icon='TRIA_LEFT').back = True
        row.operator('screenextra.frame_skip',
        text="", icon='TRIA_RIGHT').back = False
        row.label("secs")
        row.operator("sequencer.strip_jump", icon="PLAY_REVERSE", text="").next=False
        row.operator("sequencer.strip_jump", icon='PLAY', text="").next=True
        row.label("cuts")
        row.operator("screen.marker_jump", icon="TRIA_LEFT", text="").next=False
        row.operator("screen.marker_jump", icon='TRIA_RIGHT', text="").next=True
        row.label("markers")
        
        row=layout.row(align=True)
        row.operator("sequencer.refresh_all")
        row.operator('sequencer.rendersize', text='set render size', icon='PLUGIN')
        row.prop(prefs, "mini_extra_actions", text="mini ui")
        row.prop(prefs, "extra_actions_panel_show_info", text="strip info")
        
        if prefs.mini_extra_actions:
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
            row.operator('sequencerextra.jogshuttle',
                text='Jog/Shuttle', icon='NDOF_TURN')            
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
            row=layout.row(align=True)
            row.operator_menu_enum('sequencerextra.fadeinout',
            'mode', text='Fade', icon='MOD_ARRAY')
            row.operator_menu_enum('sequencerextra.copyproperties',
            'prop', icon='SCRIPT')
            
        
        if prefs.extra_actions_panel_show_info:
            layout = self.layout
            box = layout.box()
            row = box.split(percentage=0.2)
            row.label(text="Strip:")
            row.prop(strip, "name", text="")

            row = box.split(percentage=0.3)
            row.prop(strip, "type", text="")
            if strip.type == 'COLOR':
                row.prop(strip, "color", text="") 
            # show the filename source
            if strip.type in {'MOVIE', 'SOUND'}:
                row.prop(strip, "filepath", text="")
            if strip.type == 'IMAGE':
                row.prop(strip, "directory", text="")
                row = box.row(align=True)
                # Current element for the filename
                elem = strip.strip_elem_from_frame(context.scene.frame_current)
                if elem:
                    split = row.split(percentage=0.3)
                    split.label(text="File:")
                    split = split.row(align=True)
                    split.prop(elem, "filename", text="")  # strip.elements[0] could be a fallback
                row.operator("sequencer.change_path", text="change files")

            row = box.split(percentage=0.5)
            row.prop(strip, "channel")
            row.prop(strip, "frame_final_duration")
            
            row = box.row(align=True)
            row.prop(prefs, "extra_actions_panel_show_trim", text="show trim")
            if prefs.extra_actions_panel_show_trim:
                if not isinstance(strip, bpy.types.EffectSequence):
                    col = box.row(align=True)
                    col.label(text="hard:")
                    col.prop(strip, "animation_offset_start", text="Start")
                    col.prop(strip, "animation_offset_end", text="End")
                col = box.row(align=True)
                col.label(text="soft:")
                col.prop(strip, "frame_offset_start", text="Start")
                col.prop(strip, "frame_offset_end", text="End")
                
            row.prop(prefs, "extra_actions_panel_show_extra", text="show extra data")
        
        
            if prefs.extra_actions_panel_show_extra:
                box = layout.box()
                if strip.type not in {'SOUND'}:
                    row = box.row(align=True)
                    sub = row.row(align=True)
                    sub.active = (not strip.mute)
                    sub.prop(strip, "blend_alpha", text="Opacity", slider=True)
                    row.prop(strip, "mute", toggle=True, icon_only=True)
                    row.prop(strip, "lock", toggle=True, icon_only=True)

                    col = box.row(align=True)
                    col.prop(strip, "use_translation", text="Image Offset")
                    if strip.use_translation:
                            col = box.row(align=True)
                            col.prop(strip.transform, "offset_x", text="X")
                            col.prop(strip.transform, "offset_y", text="Y")
                            col = box.row(align=True)
                    col.prop(strip, "use_crop", text="Image Crop")
                    if strip.use_crop:
                        col = box.row(align=True)
                        col.prop(strip.crop, "max_y")
                        col.prop(strip.crop, "min_x")
                        col = box.row(align=True)
                        col.prop(strip.crop, "min_y")
                        col.prop(strip.crop, "max_x")
                        
                    row = box.row(align=True)
                    split = box.split(percentage=0.3)
                    split.label(text="Blend:")
                    split.prop(strip, "blend_type", text="")
                    split.prop(strip, "use_float", text="Float")
                    
                    col = box.row(align=True)
                    col.prop(strip, "color_saturation", text="Saturation")
                    col.prop(strip, "color_multiply", text="Multiply")
                    
                #sound type
                else:
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

        

        


        
        

        









