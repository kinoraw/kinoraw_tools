# Kinoraw Tools

a compilation of tools to improve video editing with blender's VSE

(Tested with blender 2.74)



*Bli bli bli bla bli bla bli bli, Bli bli bli bla* **http://kinoraw.net** *bli bla bli bli, Bli bli bli* **FLOSS video editing** *bla bli bla bli bli, Bli bli bli* **[BLENDER!](http://www.blender.org)** *bla bli bla bli bli, Bli bli bli bla* **[Jump to Cut](http://wiki.blender.org/index.php/Extensions:2.6/Py/Scripts/Sequencer/Jump_to_cut)** *bli bla bli bli, Bli bli bli* **[Extra Sequencer Actions](http://wiki.blender.org/index.php/Extensions:2.6/Py/Scripts/Sequencer/Extra_Sequencer_Actions)** *bla bli bla bli bli, Bli bli bli bla bli bla bli bli, Bli bli bli* FCP XDXDXDXD *bla bli bla bli bli, Bli bli* **useful tools grouped in the same panel** *bli bla bli bla bli bli, Bli bli bli bla bli bla bli bli. Bli bla bla bli* **fast video editing** *bli, bli bli* **with Blender** *bli bla* **linux, of course.** *Bli bla bli bli blau*

	-- Carlos Padial, 2015 ;)


<img align="center" width="500px" src="/imgs/full_screen.jpg">


## How to Install

### install the zip package (STABLE VERSION)

    The source in this repo is a **development** version
    and **maybe unstable**. 
    To get the most **stable version** follow this instructions:

* Download the zip file from this page https://github.com/kinoraw/kinoraw_repo and extract it somewhere.

* Once in Blender, open the user preferences window (ctrl+alt+u) and load the zip file named *kinoraw_tools_Vxxx.zip* with the button 'install from file' you can find at the bottom of the window.

* After that, you should activate the addon by presing the checkbox next to the addon 

<img align="center" width="500px" src="/imgs/kinoraw_addon.png">

    Every panel can be switched visible/invisible in the addon preferences panel.


### Clone the repo (DEVELOPMENT VERSION)

You can clone the addon directly in the blender addons folder, i.e: in my ubuntu computer i had to do:

    cd ~/.config/blender/2.74/scripts/addons

    git clone https://github.com/kinoraw/kinoraw_tools

then you can start blender and activate the addon in the user preferences window.


<img align="right" width="280px" src="/imgs/full_panel.png">


**Table of Contents**

- [Kinoraw Tools](#)
	- [How to Install](#how-to-install)
	- [Jump to Cut 6](#jump-to-cut-6)
		- [Main Controls](#main-controls)
		- [VSE fundamentals](#vse-fundamentals)
		- [Trim Timeline Tools](#trim-timeline-tools)
	- [Extra Tools](#extra-tools)
		- [Snap and Handles](#snap-and-handles)
		- [Meta Tools](#meta-tools)
	- [IN and OUT Tools](#in-and-out-tools)
	- [Extra Sequencer Actions](#extra-sequencer-actions)
	- [Strip Data](#strip-data)
	- [View Modifiers](#view-modifiers)
	- [Extra Data](#extra-data)
	- [Menus](#menus)
		- [VSE Header Menu > strip](#vse-header-menu--strip)
		- [VSE Header Menu > select](#vse-header-menu--select)
		- [VSE Header Menu > add](#vse-header-menu--add)
		- [VSE Header Menu > input](#vse-header-menu--input)
		- [MovieClip Editor Header Menu > Clip](#movieclip-editor-header-menu--clip)
		- [Timeline Header Menu > frame](#timeline-header-menu--frame)
	- [Proxy Tools WIP](#proxy-tools)
	- [Audio Tools WIP](#audio-tools)
	- [Exif info panel WIP](#exif-info-panel)
	- [Eco Tools    (WARNING!: CPU INTENSIVE:)](#eco-tools----warning-cpu-intensive)
	- [Random Editor panel WIP (EXPERIMENTAL)](#random-editor-panel-experimental)
	- [Glitch panel WIP (EXPERIMENTAL)](#glitch-panel-experimental)

## Jump to Cut 6

**[Jump to Cut](http://wiki.blender.org/index.php/Extensions:2.6/Py/Scripts/Sequencer/Jump_to_cut)** has been there for a while (in October will fulfill five years!) and it's still running to help you keep important things together when editing video with blender.

Since version 2.73 there is an option to jump to edit points, so Jump to Cut's original feature has been integrated into Blender code !!  =)

<img align="" src="/imgs/jump_to_cut_panel_001.png">

### Main Controls

<img align="" src="/imgs/jumpers.png">

##### Seconds 

Skip through the Timeline by one-second increments. The number of frames to skip is based on render settings for current scene. The script enables two new key bindings:

* shortcut keys **ctrl + shift + left arrow** to skip back one second,
* shortcut keys **ctrl + shift + right arrow** to skip forward one second. 

##### Cuts

The timeline cursor jumps from edit point to edit point. Edit point is any point of entry or departure of a clip, or the cutting start and end. 

* shortcut keys **Q** and **W**   

(it is assigned by default to **PgUp** and **PgDown**)

**This buttons are shortcuts for the new internal operator (added recently in Gooseberry project)**


##### Markers

As you can guess, jump from marker to marker.

* shortcut keys **alt + Q** and **alt + W**  

### VSE fundamentals

<img align="" src="/imgs/maincontrols.png">

This are self explanatory, some useful internal operators...

### Trim Timeline Tools

* TODO: use also preview timeline!!

<img align="" src="/imgs/trimmers.png">

##### In / Out

Set start and end frames of current scene according to In and Out markers.

##### Selection

Set start and end frames of current scene to match selected strips in the Sequence Editor.

It also centers the view into the selection

##### All

Set start and end frames of current scene according to the content of the Sequence Editor.

It also centers the view into the selection

## Extra Tools

Many of the following operators are from the addon **[Extra Sequencer Actions](http://wiki.blender.org/index.php/Extensions:2.6/Py/Scripts/Sequencer/Extra_Sequencer_Actions)** made in 2012 by **[Turi Scandurra](http://www.turiscandurra.com/)**

<img align="" src="/imgs/jump_to_cut_tools2.png">

*Bli bli bli* **mini UI** *bla bli bla bli bli,* **full size buttons** *Bli bli bli bla bli bla bli bli*

<img align="" src="/imgs/jump_to_cut_tools3.png">

*Bli bli bli bla bli bla bli bli,* **in/out tools** *Bli bli bli bla bli bla* **invasive features** *bli bli Bli bli bli bla bli bla bli, bli bli bli bla bli* **deactivated by default** *bla bli. Bli bli bli bla bli bla bli*

<img align="" src="/imgs/jump_to_cut_tools1.png">


### Snap and Handles

<img align="" src="/imgs/snap2.png">

<img align="" src="/imgs/snap.png">

##### Snap 

This are self explanatory, otherwise you can test and see what happens...

##### Handle selector

This are self explanatory, otherwise you can test and see what happens...

### Meta Tools

<img align="" src="/imgs/meta_tools2.png">

<img align="" src="/imgs/meta_tools.png">

##### Meta + Copy

This operator makes a metastrip with all selected items, and trim them to in and out.
If there is no IN and OUT markers, the meta is not trimmed.

##### Paste + Snap

Paste the clipboard content starting at the timeline cursor.

##### Un-meta + Trim

The selected meta is ungrouped and all related strips outside in and out range are trimmed.


## IN and OUT Tools

<img align="" src="/imgs/io_tools4.png">

<img align="" src="/imgs/io_tools2.png">

##### set IN / set OUT:

Create a marker IN and a marker OUT where the timeline cursor are. Two specific markers that can then be used for editing.

##### Selected:

Create a marker IN at the selected strip start frame and a marker OUT at the selected strip end frame.

##### Trim:

Trim (soft cut) the selected clip on both sides to adhere to the In and Out markers, as long as the clip is within that range. If not, or in absence of In and Out, does nothing. I.E. It is a quick option to cut many clips at the same duration.

##### Auto Markers

Bli bli bla bla

<img align="" src="/imgs/io_tools3.png">

<img align="" src="/imgs/io_tools.png">
 

If automarkers is selected, each scene stores his owns IN and OUT markers and you can move it only with this tools...

You can access this in and out markers with this:

    bpy.data.scenes['Scene'].kr_in_marker

    bpy.data.scenes['Scene'].kr_out_marker

## Extra Sequencer Actions

<img align="" src="/imgs/extra.png">


<img align="" src="/imgs/extra1.png">

##### Jog/Shuttle

Jog through current sequence, looping between start and end frames. This action is known as jogging, shuttling or scrubbing. Click the operator to enter interactive mode. Move mouse cursor along X axis to jog. To exit, click left or right mouse button or hit ESC.

##### Navigate Up

Move current view to parent timeline. Only enabled when current view is relative to a Meta strip. This operator does not perform any modification to timeline elements.

##### Extend to Fill

Extend active strip forward to fill adjacent space. If there no other strip is following active one on the same channel, the clip is extended to the end of the sequence.

<img align="" src="/imgs/extra2.png">

##### File Place

Place active file from File Browser to Sequencer Editor on current frame.

##### File Insert

Same as above, but also move forward all strips after current frame.

##### Slip

Alter in and out points of a strip but not its duration. Only available when a the type of active strip is Movie, Scene or Meta. Click 'Input...' to choose the amount of sliding desired. The start and end frame of active strip will be moved, but its length and position will remain unchanged.

Interactive mode. Move mouse cursor along X axis to jog. To exit, click left or right mouse button or hit ESC.

**This button is shortcut for the new internal operator (added recently in Gooseberry project)**

<img align="" src="/imgs/extra3.png">

##### Fade

Fade opacity of active strip, or its volume if its type is Sound, creating keyframes for the corresponding property. Possible fade directions are In, Out, In and Out. Duration defines the number of frames between the start and the end of the fade. Amount defines the maximum value that the fade will set. For opacity fades, the maximum value is 1.0. The minimum value reached by the fade is always 0. Keyframes created with this operator can be manipulated through the F-Curve Editor.

##### Copy Properties

Copy properties of active strip to selected strips. Start selecting multiple strips, then make active the strip whose properties need to be copied to the selected strips. Click the desired operator to perform the action. Some operators affect single properties, while some others affect a group of properties.


## Strip Data

Bli bli bli bla bli bla bli bli, **accesible data from selected strip** Bli bli bli bla bli bla bli bli

<img align="" src="/imgs/jump_to_cut_info_movie.png">

Bli bli bli **trim information** bla bli bla bli bli, **soft & hard** Bli bli bli bla bli bla bli bli

<img align="" src="/imgs/jump_to_cut_info_color.png">

bla bli bla bli bli, **all strip types** Bli bli bli bla bli bla bli bli blau

<img align="" src="/imgs/jump_to_cut_info_wipe.png">

<img align="" src="/imgs/jump_to_cut_info_speed.png">

<img align="" src="/imgs/jump_to_cut_info_blur.png">

## View Modifiers

<img align="" src="/imgs/jump_to_cut_info_modifier.png">

bla bli bla bli bli, **same menus, less space** Bli bli bli bla bli bla bli bli blau

<img align="" src="/imgs/jump_to_cut_info_modifier2.png">

## Extra Data

Bli bli bli bla bli bla bli bli, **secondary properties** Bli bli bli bla bli bla bli bli

<img align="" src="/imgs/jump_to_cut_info_sound.png">

Bli bli bli bla bli bla bli bli, **geometry properties** Bli bli bli bla bli bla bli bli

<img align="" src="/imgs/jump_to_cut_info_image.png">


## Menus

### VSE Header Menu > strip

<img align="" src="/imgs/menu_strip.png">

##### Ripple Delete

Delete the active strip and shift back all other strips the number of frames between the beginning of deleted strip and the next edit in the sequence.

##### Ripple cut

Same as above, but copying active strip to memory buffer before deleting it. Copied strip can be pasted in place as usual, for example using the keystroke combination ctrl-V.

* **TO FIX:** ripple cut and ripple delete: some strips change their channel position
it seems to happend when one involved strips is the one in higher position...

##### insert 

Shift forward all strips after current frame and insert active strip.

* **TO FIX:** insert operator works fine but sometimes some strips change their
channel position.


##### Insert (Single Channel)

Same as above, but shifting occurs only on the same channel as active strip.


### VSE Header Menu > select

<img align="" src="/imgs/menu_select.png">

##### Select All by Type

Select all the strips of the specified type in the Sequence Editor.

##### Current-Frame-Aware Select

Select strips on all channels according to current frame. Available modes are:

* Before (select all strips before current frame),
* After (select all strips after current frame),
* On (select all strips underneath playhead). 

##### Select same channel

Select strips on the same channel as selected


### VSE Header Menu > add

<img align="" src="/imgs/menu_add.png">

##### Recursive Loader

In a File Browser area, select a file and in the VSE panel press "Import from Browser" button. All movie clips will be imported (sorted alphabeticaly by filename) in the VSE

* Check "Recursive" option to search recursively in this folder
* Check "Select by extension" to force import only files with the selected extension.
 

### VSE Header Menu > input

<img align="" src="/imgs/menu_input.png">

##### Open with Editor

Open active strip with Movie Clip Editor or Image Editor, according to strip type. If a clip is already loaded, existing data is used.

##### Open with External Editor

Open active image strip with the default external image editor. To use this operator a valid path to the external editor must be specified in User Preferences > File.

##### Create a Movieclip strip

When a movie or image strip is selected, this operator creates a movieclip or find the correspondent movieclip that already exists for this footage, and add a VSE strip with same cuts the original strip has.It can convert movie strips and image sequences, both with hard cuts or soft cuts.

##### File Name to Strip Name

Set strip name to input file name. This operator is useful after separating images of a sequence.

### MovieClip Editor Header Menu > Clip

<img align="" src="/imgs/menu_movieclip.png">

##### Open from File Browser

Bli bla bli bla bla

##### Open Active Strip

Bli bla bli bli blau

### Timeline Header Menu > frame

<img align="" src="/imgs/menu_frame.png">

##### Skip One Second

Skip through the Timeline by one-second increments. The number of frames to skip is based on render settings for current scene. The script enables two new key bindings:

* shortcut keys **ctrl + shift + left arrow** to skip back one second,
* shortcut keys **ctrl + shift + right arrow** to skip forward one second. 

##### Trim to Selection

Set start and end frames of current scene to match selected strips in the Sequence Editor.

It also centers the view into the selection

##### Trim to Timeline Content

Set start and end frames of current scene according to the content of the Sequence Editor.

It also centers the view into the selection


## Proxy Tools

<img align="" src="/imgs/proxy_tools.png">


## Audio Tools

<img align="" src="/imgs/audio_tools.png">

### Extract WAV

create a wav file out of a selected movie strip in the indicated path.
If the audio file already exists in the path, it is loaded and trimmed according to the selected movie strip.

You can also generate ffmpeg scripts to launch a batch conversion out of blender.

### Sync Tool

This is useful to sync diferent audio strips to a single movie strip. It does not mantain the sync if you move only the movie strip, but anytime you can delete audio strips and reload again synced.

Select an audio strip and a movie strip and press **set sync** to store sync information in a text file. 

Press **reload audio** with a movie strip selected to reload the audio files

## Exif info panel

<img align="" src="/imgs/exif.png">

Select a strip and press 'Read EXIF data'. Works only with image and movie strips 

to get exif info panel you need to install exiftools:

    sudo apt-get install libimage-exiftool-perl


## Eco Tools    (WARNING!: CPU INTENSIVE:)

<img align="" src="/imgs/eco.png">

TODO: keep metastrip in the same channel

Only visible with a Metastrip selected

Select a movie or meta strip, set number of echoes and offset (in frames), and press Eco button.

The opacity of all strips is updated to 1/number of echoes to mantain luminance. The blending is set to alpha over for all clips except first one.

If add mode is selected, the blending is set to add.

All clips are finally grouped inside a meta. Press home after running the script to see the meta.


## Random Editor panel (EXPERIMENTAL)

Only visible with a Metastrip selected

<img align="" src="/imgs/random_editor.png">

###Random Scratch Operator

Given *IN and OUT* points, a *duration* in frames, and a Meta as *source*, the operator populates the in and out range with random cuts from source, all with the same *duration*

### Random Editor Operator

Not working yet!

## Glitch panel (EXPERIMENTAL)

<img align="" src="/imgs/glitch.png">

for the moment it has only glitch algorithm, you need to install aviglitch
more info here:

 http://ucnv.github.io/aviglitch/


cc-by: **[Carlos Padial](http://surreal.asturnazari.com)**, 2015 