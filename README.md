# Kinoraw Tools

a compilation of addons to improve video editing with blender's VSE

(Tested with blender 2.74)

![kinoraw addon](/imgs/kinoraw_addon.png?raw=true "kinoraw addon")

Bli bli bli bla bli bla bli bli, Bli bli bli bla **http://kinoraw.net** bli bla bli bli, Bli bli bli bla bli bla bli bli, Bli bli bli bla bli bla bli bli, Bli bli bli bla **[JumptoCut](http://wiki.blender.org/index.php/Extensions:2.6/Py/Scripts/Sequencer/Jump_to_cut)** bli bla bli bli, Bli bli bli **[Extra Sequencer Actions](http://wiki.blender.org/index.php/Extensions:2.6/Py/Scripts/Sequencer/Extra_Sequencer_Actions)** bla bli bla bli bli, Bli bli bli bla bli bla bli bli, Bli bli bli bla bli bla bli bli, Bli bli bli bla bli bla bli bli, Bli bli bli bla bli bla bli bli, Bli **[Eco](http://wiki.blender.org/index.php/Extensions:2.6/Py/Scripts/Sequencer/Eco)** bli bli bla bli bla bli bli, Bli bli bli bla bli bla bli bli, 

## Jump to Cut panel

Bli bli bli bla bli bla bli bli, Bli bli bli bla bli bla bli bli, Bli bli bli bla bli bla bli bli

### Main Controls

Bli bli bli bla bli bla bli bli, Bli bli bli bla bli bla bli bli

![kinoraw addon](/imgs/jump_to_cut_panel_001.png?raw=true "kinoraw addon")

#### Trim to Timeline Content

Automatically set start and end frames of current scene according to the content of the Sequence Editor.

#### Trim to Selection

Set start and end frames of current scene to match selected strips in the Sequence Editor.

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

#### Trim + Meta + Copy:

This operator makes a metastrip with all selected items, and trim them to in and out, There is not an insert edit, but also streamlines the tasks a bit ...

If there is no IN and OUT markers, the meta is not trimmed.

#### Paste + Snap:

Paste the clipboard content aligned at the timeline cursor.

![kinoraw addon](/imgs/io_tools.png?raw=true "kinoraw addon")

#### IN / OUT:

Create a marker IN and a marker OUT where the timeline cursor are. Two specific markers that can then be used for editing.

#### Mark in & out to active strip:

Create a marker IN at the selected strip start frame and a marker OUT at the selected strip end frame.

#### Trim to in & out:

Trim (soft cut) the selected clip on both sides to adhere to the In and Out markers, as long as the clip is within that range. If not, or in absence of In and Out, does nothing. I.E. It is a quick option to cut many clips at the same duration.

#### Set Start & End:

Set scene start and end frames with the same values of IN and OUT markers.

 

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

#### Slide Grab

Same as above, interactive mode. Move mouse cursor along X axis to jog. To exit, click left or right mouse button or hit ESC.

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

    Before (select all strips before current frame),
    After (select all strips after current frame),
    On (select all strips underneath playhead). 

### VSE Header Menu > add

![kinoraw addon](/imgs/menu_add.png?raw=true "kinoraw addon")

####Recursive Loader

In a File Browser area, select a file and in the VSE panel press "Import from Browser" button. All movie clips will be imported (sorted alphabeticaly by filename) in the VSE

    Check "Recursive" option to search recursively in this folder
    Check "Same extension" to force import only files with the selected extension.
    Check "Proxies" to setup proxies if existing. (first load a single file with Proxy Place to setup extension and suffix) 

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


## Exif info panel

![kinoraw addon](/imgs/exif.png?raw=true "kinoraw addon")

Select a strip and press 'Read EXIF data'. Works only with image and movie strips 

to get exif info panel you need to install exiftools:

    sudo apt-get install libimage-exiftool-perl


## Eco Tools

![kinoraw addon](/imgs/eco.png?raw=true "kinoraw addon")

Only visible with a Metastrip selected

for eco tools check:

http://wiki.blender.org/index.php/Extensions:2.6/Py/Scripts/Sequencer/Eco

## Random Editor panel

Only visible with a Metastrip selected

![kinoraw addon](/imgs/random_editor.png?raw=true "kinoraw addon")

## Glitch panel

![kinoraw addon](/imgs/glitch.png?raw=true "kinoraw addon")

EXPERIMENTAL!! 

Only visible with a Metastrip selected

















#### Open from File Browser

Load a Movie or Image Sequence from File Browser to Movie Clip Editor. If a clip is already loaded, existing data is used.

#### Open Active Strip

Load a Movie or Image Sequence from Sequence Editor to Movie Clip Editor. If a clip is already loaded, existing data is used.

#### Skip One Second

Skip through the Timeline by one-second increments. The number of frames to skip is based on render settings for current scene. The script enables two new key bindings:

    ctrl + shift + left arrow to skip back one second,
    ctrl + shift + right arrow to skip forward one second. 





