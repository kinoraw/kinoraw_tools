# Kinoraw Tools

a compilation of addons to improve video editing with blender's VSE

(Tested with blender 2.74)

![kinoraw addon](/imgs/kinoraw_addon.png?raw=true "kinoraw addon")

Bli bli bli bla bli **useful tools grouped in the same panel** bla bli bli, Bli bli bli bla **http://kinoraw.net** bli bla bli bli, Bli bli bli bla bli bla bli bli, Bli bli bli bla bli bla bli bli, Bli bli bli bla **[JumptoCut](http://wiki.blender.org/index.php/Extensions:2.6/Py/Scripts/Sequencer/Jump_to_cut)** bli bla bli bli, Bli bli bli **[Extra Sequencer Actions](http://wiki.blender.org/index.php/Extensions:2.6/Py/Scripts/Sequencer/Extra_Sequencer_Actions)** bla bli bla bli bli, Bli bli bli bla bli bla bli bli, Bli bli bli bla bli bla bli bli, Bli bli bli bla bli bla bli bli, Bli bli bli bla bli bla bli bli, Bli **[Eco](http://wiki.blender.org/index.php/Extensions:2.6/Py/Scripts/Sequencer/Eco)** bli bli bla bli bla bli bli, Bli bli bli bla bli bla bli bli, 

## Jump to Cut 6

Jump to Cut has been there for a while (in October will fulfill five years!) and it's still running to help you keep important things together when editing video with blender.

Bli bli bli bla bli bla bli bli, Bli bli bli bla bli bla bli bli, Bli bli bli bla bli bla bli bli

### Main Controls

Bli bli bli bla bli bla bli bli, Bli bli bli bla bli bla bli bli

![kinoraw addon](/imgs/jump_to_cut_panel_001.png?raw=true "kinoraw addon")

![kinoraw addon](/imgs/jumpers.png?raw=true "kinoraw addon")



![kinoraw addon](/imgs/trimmers.png?raw=true "kinoraw addon")

#### In / Out (Trim to In and Out)

Automatically set start and end frames of current scene according to In and Out markers.

#### Selection (Trim to Selection)

Set start and end frames of current scene to match selected strips in the Sequence Editor.

#### All (Trim to Timeline Content)

Automatically set start and end frames of current scene according to the content of the Sequence Editor.

### Extra Tools

Bli bli bli bla bli bla bli bli, **sequencer extra actions** Bli bli bli bla bli bla bli bli

![kinoraw addon](/imgs/jump_to_cut_tools2.png?raw=true "kinoraw addon")

Bli bli bli bla bli bla bli bli, **in/out tools** Bli bli bli bla bli bla bli bli

![kinoraw addon](/imgs/jump_to_cut_tools1.png?raw=true "kinoraw addon")

Bli bli bli bla bli bla bli bli, **full size buttons** Bli bli bli bla bli bla bli bli

![kinoraw addon](/imgs/jump_to_cut_tools3.png?raw=true "kinoraw addon")


![kinoraw addon](/imgs/snap.png?raw=true "kinoraw addon")

#### Snap 

#### Handle selector

![kinoraw addon](/imgs/meta_tools.png?raw=true "kinoraw addon")

#### Meta + Copy

This operator makes a metastrip with all selected items, and trim them to in and out.
If there is no IN and OUT markers, the meta is not trimmed.

#### Paste + Snap

Paste the clipboard content starting at the timeline cursor.

#### Un-meta + Trim

![kinoraw addon](/imgs/io_tools2.png?raw=true "kinoraw addon")

#### set IN / set OUT:

Create a marker IN and a marker OUT where the timeline cursor are. Two specific markers that can then be used for editing.

#### Selected:

Create a marker IN at the selected strip start frame and a marker OUT at the selected strip end frame.

#### Trim:

Trim (soft cut) the selected clip on both sides to adhere to the In and Out markers, as long as the clip is within that range. If not, or in absence of In and Out, does nothing. I.E. It is a quick option to cut many clips at the same duration.

#### Auto Markers

Bli bli bla bla

![kinoraw addon](/imgs/io_tools.png?raw=true "kinoraw addon")
 

If automarkers is selected, each scene stores his owns IN and OUT markers and you can move it only with this tools...

You can access this in and out markers with this:

bpy.data.scenes['Scene']


![kinoraw addon](/imgs/extra1.png?raw=true "kinoraw addon")

#### Jog/Shuttle

Jog through current sequence, looping between start and end frames. This action is known as jogging, shuttling or scrubbing. Click the operator to enter interactive mode. Move mouse cursor along X axis to jog. To exit, click left or right mouse button or hit ESC.

#### Navigate Up

Move current view to parent timeline. Only enabled when current view is relative to a Meta strip. This operator does not perform any modification to timeline elements.

#### Extend to Fill

Extend active strip forward to fill adjacent space. If there no other strip is following active one on the same channel, the clip is extended to the end of the sequence.

![kinoraw addon](/imgs/extra2.png?raw=true "kinoraw addon")

#### File Place

Place active file from File Browser to Sequencer Editor on current frame.

#### File Insert

Same as above, but also move forward all strips after current frame.

#### Slip

Alter in and out points of a strip but not its duration. Only available when a the type of active strip is Movie, Scene or Meta. Click 'Input...' to choose the amount of sliding desired. The start and end frame of active strip will be moved, but its length and position will remain unchanged.

Interactive mode. Move mouse cursor along X axis to jog. To exit, click left or right mouse button or hit ESC.

![kinoraw addon](/imgs/extra3.png?raw=true "kinoraw addon")

#### Fade

Fade opacity of active strip, or its volume if its type is Sound, creating keyframes for the corresponding property. Possible fade directions are In, Out, In and Out. Duration defines the number of frames between the start and the end of the fade. Amount defines the maximum value that the fade will set. For opacity fades, the maximum value is 1.0. The minimum value reached by the fade is always 0. Keyframes created with this operator can be manipulated through the F-Curve Editor.

#### Copy Properties

Copy properties of active strip to selected strips. Start selecting multiple strips, then make active the strip whose properties need to be copied to the selected strips. Click the desired operator to perform the action. Some operators affect single properties, while some others affect a group of properties.


### Strip Data

Bli bli bli bla bli bla bli bli, **accesible data from selected strip** Bli bli bli bla bli bla bli bli

![kinoraw addon](/imgs/jump_to_cut_info_movie.png?raw=true "kinoraw addon")

Bli bli bli **trim information** bla bli bla bli bli, **soft & hard** Bli bli bli bla bli bla bli bli

![kinoraw addon](/imgs/jump_to_cut_info_color.png?raw=true "kinoraw addon")

bla bli bla bli bli, **all strip types** Bli bli bli bla bli bla bli bli blau

![kinoraw addon](/imgs/jump_to_cut_info_wipe.png?raw=true "kinoraw addon")

![kinoraw addon](/imgs/jump_to_cut_info_speed.png?raw=true "kinoraw addon")

![kinoraw addon](/imgs/jump_to_cut_info_blur.png?raw=true "kinoraw addon")

### View Modifiers

![kinoraw addon](/imgs/jump_to_cut_info_modifier.png?raw=true "kinoraw addon")

bla bli bla bli bli, **same menus, less space** Bli bli bli bla bli bla bli bli blau

![kinoraw addon](/imgs/jump_to_cut_info_modifier2.png?raw=true "kinoraw addon")

### Extra Data

Bli bli bli bla bli bla bli bli, **secondary properties** Bli bli bli bla bli bla bli bli

![kinoraw addon](/imgs/jump_to_cut_info_sound.png?raw=true "kinoraw addon")

Bli bli bli bla bli bla bli bli, **geometry properties** Bli bli bli bla bli bla bli bli

![kinoraw addon](/imgs/jump_to_cut_info_image.png?raw=true "kinoraw addon")


## VSE Header Menu

### VSE Header Menu > strip

![kinoraw addon](/imgs/menu_strip.png?raw=true "kinoraw addon")

#### Ripple Delete  (TODO: FIX)

Delete the active strip and shift back all other strips the number of frames between the beginning of deleted strip and the next edit in the sequence.

#### Ripple cut    (TODO: FIX)

Same as above, but copying active strip to memory buffer before deleting it. Copied strip can be pasted in place as usual, for example using the keystroke combination ctrl-V.

#### Insert

Shift forward all strips after current frame and insert active strip.

#### Insert (Single Channel)

Same as above, but shifting occurs only on the same channel as active strip.


### VSE Header Menu > select

![kinoraw addon](/imgs/menu_select.png?raw=true "kinoraw addon")

#### Select All by Type

Select all the strips of the specified type in the Sequence Editor.

#### Current-Frame-Aware Select

Select strips on all channels according to current frame. Available modes are:

* Before (select all strips before current frame),
* After (select all strips after current frame),
* On (select all strips underneath playhead). 

#### Select same channel

### VSE Header Menu > add

![kinoraw addon](/imgs/menu_add.png?raw=true "kinoraw addon")

####Recursive Loader

In a File Browser area, select a file and in the VSE panel press "Import from Browser" button. All movie clips will be imported (sorted alphabeticaly by filename) in the VSE

* Check "Recursive" option to search recursively in this folder
* Check "Select by extension" to force import only files with the selected extension.
 

### VSE Header Menu > input

![kinoraw addon](/imgs/menu_input.png?raw=true "kinoraw addon")

#### Open with Editor

Open active strip with Movie Clip Editor or Image Editor, according to strip type. If a clip is already loaded, existing data is used.

#### Open with External Editor

Open active image strip with the default external image editor. To use this operator a valid path to the external editor must be specified in User Preferences > File.

#### Create a Movieclip strip

When a movie or image strip is selected, this operator creates a movieclip or find the correspondent movieclip that already exists for this footage, and add a VSE strip with same cuts the original strip has.It can convert movie strips and image sequences, both with hard cuts or soft cuts.

#### File Name to Strip Name

Set strip name to input file name. This operator is useful after separating images of a sequence.

## MovieClip Editor Header Menu

### MovieClip Editor Header Menu > Clip

![kinoraw addon](/imgs/menu_movieclip.png?raw=true "kinoraw addon")

## Timeline Header Menu

### Timeline Header Menu > frame

![kinoraw addon](/imgs/menu_frame.png?raw=true "kinoraw addon")


## Proxy Tools

![kinoraw addon](/imgs/proxy_tools.png?raw=true "kinoraw addon")


## Audio Tools

![kinoraw addon](/imgs/audio_tools.png?raw=true "kinoraw addon")

### EXTRACT WAV

create a wav file out of a selected movie strip in the indicated path.
If the audio file already exists in the path, it is loaded and trimmed according to the selected movie strip.

You can also generate ffmpeg scripts to launch a batch conversion out of blender.

### sync tool

This is useful to sync diferent audio strips to a single movie strip. It does not mantain the sync if you move only the movie strip, but anytime you can delete audio strips and reload again synced.

Select an audio strip and a movie strip and press **set sync** to store sync information in a text file. 

Press **reload audio** with a movie strip selected to reload the audio files

## Exif info panel

![kinoraw addon](/imgs/exif.png?raw=true "kinoraw addon")

Select a strip and press 'Read EXIF data'. Works only with image and movie strips 

to get exif info panel you need to install exiftools:

    sudo apt-get install libimage-exiftool-perl


## Eco Tools    (WARNING!: CPU INTENSIVE:)

![kinoraw addon](/imgs/eco.png?raw=true "kinoraw addon")

TODO: keep metastrip in the same channel

Only visible with a Metastrip selected

Select a movie or meta strip, set number of echoes and offset (in frames), and press Eco button.

The opacity of all strips is updated to 1/number of echoes to mantain luminance. The blending is set to alpha over for all clips except first one.

If add mode is selected, the blending is set to add.

All clips are finally grouped inside a meta. Press home after running the script to see the meta.


## Random Editor panel (EXPERIMENTAL)

Only visible with a Metastrip selected

![kinoraw addon](/imgs/random_editor.png?raw=true "kinoraw addon")

###Random Scratch Operator

Given *IN and OUT* points, a *duration* in frames, and a Meta as *source*, the operator populates the in and out range with random cuts from source, all with the same *duration*

### Random Editor Operator

Not working yet!

## Glitch panel (EXPERIMENTAL)

![kinoraw addon](/imgs/glitch.png?raw=true "kinoraw addon")



















#### Open from File Browser

Load a Movie or Image Sequence from File Browser to Movie Clip Editor. If a clip is already loaded, existing data is used.

#### Open Active Strip

Load a Movie or Image Sequence from Sequence Editor to Movie Clip Editor. If a clip is already loaded, existing data is used.

#### Skip One Second

Skip through the Timeline by one-second increments. The number of frames to skip is based on render settings for current scene. The script enables two new key bindings:

    ctrl + shift + left arrow to skip back one second,
    ctrl + shift + right arrow to skip forward one second. 





