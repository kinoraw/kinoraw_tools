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
import os.path, operator, subprocess, random

from bpy.props import IntProperty
from bpy.props import FloatProperty
from bpy.props import EnumProperty
from bpy.props import BoolProperty
from bpy.props import StringProperty

imb_ext_image = [
    # IMG
    ".png", ".tga", ".bmp", ".jpg", ".jpeg", ".sgi", ".rgb",
    ".rgba", ".tif", ".tiff", ".tx", ".jp2", ".hdr", ".dds",
    ".dpx", ".cin", ".exr", ".rw2",
    # IMG QT
    ".gif", ".psd", ".pct", ".pict", ".pntg", ".qtif"]


imb_ext_movie = [
    ".avi", ".flc", ".mov", ".movie", ".mp4", ".m4v", ".m2v",
    ".m2t", ".m2ts", ".mts", ".mv", ".avs", ".wmv", ".ogv",
    ".dv", ".mpeg", ".mpg", ".mpg2", ".vob", ".mkv", ".flv",
    ".divx", ".xvid", ".mxf"]
    
movieextdict = [("1", ".avi", ""),
            ("2", ".flc", ""),
            ("3", ".mov", ""),
            ("4", ".movie", ""),
            ("5", ".mp4", ""),
            ("6", ".m4v", ""),
            ("7", ".m2v", ""),
            ("8", ".m2t", ""),
            ("9", ".m2ts", ""),
            ("10", ".mts", ""),
            ("11", ".mv", ""),
            ("12", ".avs", ""),
            ("13", ".wmv", ""),
            ("14", ".ogv", ""),
            ("15", ".dv", ""),
            ("16", ".mpeg", ""),
            ("17", ".mpg", ""),
            ("18", ".mpg2", ""),
            ("19", ".vob", ""),
            ("20", ".mkv", ""),
            ("21", ".flv", ""),
            ("22", ".divx", ""),
            ("23", ".xvid", ""),
            ("24", ".mxf", "")]


# Functions

# initSceneProperties is ONLY for varaibles that should 
# be keeped with the blend file. Any other addon preferences
# should go to the addon preferences operator in __init__
# TODO: recode operator_exta_actions.py
def initSceneProperties(context):
    try:
        if context.scene.scene_initialized == True:
            return False
    except AttributeError:
        pass

    scn = context.scene

    bpy.types.Scene.auto_markers = BoolProperty(
        name='auto_markers',
        description='activate auto markers',
        default=True)
    scn.auto_markers = True

    bpy.types.Scene.in_marker = IntProperty(
        name='in',
        description='in frame position',
        min=-30000, max=30000,
        default=0)
    scn.in_marker = 0

    bpy.types.Scene.out_marker = IntProperty(
        name='out',
        description='out frame position',
        min=scn.in_marker, max=30000,
        default=250)
    scn.out_marker = 250

    bpy.types.Scene.default_fade_duration = IntProperty(
        name='Duration',
        description='Number of frames to fade',
        min=1, max=250,
        default=scn.render.fps)
    scn.default_fade_duration = scn.render.fps

    bpy.types.Scene.default_fade_amount = FloatProperty(
        name='Amount',
        description='Maximum value of fade',
        min=0.0,
        max=100.0,
        default=1.0)
    scn.default_fade_amount = 1.0

    bpy.types.Scene.default_distribute_offset = IntProperty(
        name='Offset',
        description='Number of frames between strip start frames',
        min=1,
        max=250,
        default=2)
    scn.default_distribute_offset = 2

    bpy.types.Scene.default_distribute_reverse = BoolProperty(
        name='Reverse Order',
        description='Reverse the order of selected strips',
        default=False)
    scn.default_distribute_reverse = False

    bpy.types.Scene.default_recursive = BoolProperty(
        name='Recursive',
        description='Load in recursive folders',
        default=False)
    scn.default_recursive = False

    bpy.types.Scene.default_recursive_select_by_extension = BoolProperty(
        name='Recursive ext',
        description='Load only clips with selected extension',
        default=False)
    scn.default_recursive_select_by_extension = False

    bpy.types.Scene.default_ext = EnumProperty(
        items=movieextdict,
        name="ext enum",
        default="3")
    scn.default_ext = "3"

    bpy.types.Scene.scene_initialized = BoolProperty(
        name='Init',
        default=False)
    scn.scene_initialized = True

    return True


def deselect_all_strips(context):
    "deselect all strips"
    for i in context.scene.sequence_editor.sequences_all:
        i.select = False

def get_selected_strips(context):
    "return a list of selected strips"
    strips=[]
    for i in context.scene.sequence_editor.sequences_all:
        if i.select == True:
            strips.append(i)
    return strips

def activate_strip(context,strip):
    "select and activate strip"
    context.scene.sequence_editor.active_strip = strip

def create_folder(path):
    if not os.path.isdir(bpy.path.abspath(path)):
        folder = bpy.path.abspath(path)
        command = "mkdir "+folder
        subprocess.call(command,shell=True)


def add_marker(context, text):
    scene = context.scene
    markers = scene.timeline_markers
    mark = markers.new(name=text)
    mark.frame = scene.frame_current


def act_strip(context):
    try:
        return context.scene.sequence_editor.active_strip
    except AttributeError:
        return None


def detect_strip_type(filepath):
    imb_ext_image = [
    # IMG
    ".png", ".tga", ".bmp", ".jpg", ".jpeg", ".sgi", ".rgb",
    ".rgba", ".tif", ".tiff", ".tx", ".jp2", ".hdr", ".dds",
    ".dpx", ".cin", ".exr",
    # IMG QT
    ".gif", ".psd", ".pct", ".pict", ".pntg", ".qtif"]

    imb_ext_movie = [
    ".avi", ".flc", ".mov", ".movie", ".mp4", ".m4v", ".m2v",
    ".m2t", ".m2ts", ".mts", ".mv", ".avs", ".wmv", ".ogv", ".ogg",
    ".dv", ".mpeg", ".mpg", ".mpg2", ".vob", ".mkv", ".flv",
    ".divx", ".xvid", ".mxf"]

    imb_ext_audio = [
    ".wav", ".ogg", ".oga", ".mp3", ".mp2", ".ac3", ".aac",
    ".flac", ".wma", ".eac3", ".aif", ".aiff", ".m4a"]

    extension = os.path.splitext(filepath)[1]
    extension = extension.lower()
    if extension in imb_ext_image:
        type = 'IMAGE'
    elif extension in imb_ext_movie:
        type = 'MOVIE'
    elif extension in imb_ext_audio:
        type = 'SOUND'
    else:
        type = None

    return type


def getpathfrombrowser(context):
    '''
    returns path from filebrowser
    '''
    scn = context.scene
    for a in context.window.screen.areas:
        if a.type == 'FILE_BROWSER':
            params = a.spaces[0].params
            break
    try:
        params
    except UnboundLocalError:
        #print("no browser")
        self.report({'ERROR_INVALID_INPUT'}, 'No visible File Browser')
        return {'CANCELLED'}
    path = params.directory
    return path


def getfilepathfrombrowser(context):
    '''
    returns path and file from filebrowser
    '''
    scn = context.scene
    for a in context.window.screen.areas:
        if a.type == 'FILE_BROWSER':
            params = a.spaces[0].params
            break
    try:
        params
    except UnboundLocalError:
        #print("no browser")
        #self.report({'ERROR_INVALID_INPUT'}, 'No visible File Browser')
        return {'CANCELLED'}

    if params.filename == '':
        #print("no file selected")
        #self.report({'ERROR_INVALID_INPUT'}, 'No file selected')
        return {'CANCELLED'}
    path = params.directory
    filename = params.filename
    return path, filename


def setpathinbrowser(context, path, file):
    '''
    set path and file in the filebrowser
    '''
    scn = context.scene
    for a in context.window.screen.areas:
        if a.type == 'FILE_BROWSER':
            params = a.spaces[0].params
            break
    try:
        params
    except UnboundLocalError:
        #print("no browser")
        self.report({'ERROR_INVALID_INPUT'}, 'No visible File Browser')
        return {'CANCELLED'}

    params.directory = path
    params.filename = file
    return path, params


def sortlist(filelist):
    '''
    given a list of tuplas (path, filename) returns a list sorted by filename
    '''
    filelist_sorted = sorted(filelist, key=operator.itemgetter(1))
    return filelist_sorted
    
# recursive load functions 

def onefolder(context, recursive_select_by_extension, ext):
    '''
    returns a list of MOVIE type files from folder selected in file browser
    '''
    filelist = []
    path, filename = getfilepathfrombrowser(context)
    
    for i in movieextdict: 
        if i[0] == ext:
            extension = i[1].rpartition(".")[2]
            break

    scn = context.scene

    if detect_strip_type(path + filename) == 'MOVIE':
        if recursive_select_by_extension == True:
            #filtering by extension...
            for file in os.listdir(path):
                if file.rpartition(".")[2].lower() == extension:
                    filelist.append((path, file))
        else:
            #looking for all known extensions
            for file in os.listdir(path):
                for i in movieextdict:
                    if file.rpartition(".")[2].lower() == i[1].rpartition(".")[2]:
                        filelist.append((path, file))
    return (filelist)

def recursive(context, recursive_select_by_extension, ext):
    '''
    returns a list of MOVIE type files recursively from file browser
    '''
    filelist = []
    path = getpathfrombrowser(context)
    
    for i in movieextdict:
        if i[0] == ext:
            extension = i[1].rpartition(".")[2]
            break
    
    scn = context.scene        
    for root, dirs, files in os.walk(path):
        for file in files:
            if recursive_select_by_extension == True:
                #filtering by extension...
                if file.rpartition(".")[2].lower() == extension:
                    filelist.append((root, file))
            else:
                #looking for all known extensions
                for i in movieextdict:
                    if file.rpartition(".")[2].lower() == i[1].rpartition(".")[2]:
                        filelist.append((root, file))
    return filelist   



# jump to cut functions
def triminout(strip, sin, sout):

    """trim the strip to in and out, and returns 
    true if the strip is outside given in and out"""
    
    start = strip.frame_start + strip.frame_offset_start - strip.frame_still_start
    end = start + strip.frame_final_duration

    remove = False
    if end < sin: remove = True
    if start > sout: remove = True
    
    if end > sin:
        if start < sin:
            strip.select_right_handle = False
            strip.select_left_handle = True
            bpy.ops.sequencer.snap(frame=sin)
            strip.select_left_handle = False
    if start < sout:
        if end > sout:
            strip.select_left_handle = False
            strip.select_right_handle = True
            bpy.ops.sequencer.snap(frame=sout)
            strip.select_right_handle = False

    return remove

def searchprev(j, list):
    list.sort(reverse=True)
    for i in list:
        if i < j:
            result = i
            break
    else: result = j
    return result

def searchnext(j, list):
    list.sort()
    for i in list:
        if i > j:
            result = i
            break
    else: result = j
    return result

# not used 
def geteditpoints_old(seq):
    #this create a list of editpoints including strips from
    # inside metastrips. It reads only 1 level into the metastrip
    editpoints = []
    striplist = []
    metalist = []
    if seq:
        for i in seq.sequences:
            if i.type == 'META':
                metalist.append(i)
                start = i.frame_start + i.frame_offset_start
                end = start + i.frame_final_duration
                editpoints.append(start)
                editpoints.append(end)
            else:
                striplist.append(i)
        for i in metalist:
            for j in i.sequences:
                striplist.append(j)
        for i in striplist:
            start = i.frame_start + i.frame_offset_start
            end = start + i.frame_final_duration
            editpoints.append(start)
            editpoints.append(end)
            #print(start," ",end)
    return editpoints

def geteditpoints(context):
    #this create a list of editpoints from current meta_stack level
    scn = context.scene
    seq = scn.sequence_editor

    editpoints=[]
    striplist=[]

    if len(seq.meta_stack) > 0:
        striplist = seq.sequences_all[seq.meta_stack[len(seq.meta_stack)-1].name].sequences 
    else:
        striplist = seq.sequences

    for strip in striplist:
        i = seq.sequences_all[strip.name]
        start = i.frame_start + i.frame_offset_start - i.frame_still_start
        end = start + i.frame_final_duration 
        editpoints.append(start)
        editpoints.append(end)
    return editpoints

#------------ .........................  REVISAR

def randompartition(lst,n,rand):
    division = len(lst) / float(n)
    lista = []
    for i in range(n):	lista.append(division)
    var=0
    for i in range(n-1):
        lista[i]+= random.randint(-int(rand*division),int(rand*division))
        var+=lista[i]
    if lista[n-1] != len(lst)-var:
        lista[n-1] = len(lst)-var
    random.shuffle(lista)
    division = len(lst) / float(n)
    count = 0
    newlist=[]
    for i in range(n):
        #print(lst[count : int(lista[i]-1)+count])
        newlist.append([lst[count : int(lista[i]-1)+count]])
        count += int(lista[i]) 
    return newlist


#------------ random editor functions.

def randomframe(strip):
    #random frame between a and b
    a = strip.frame_start
    b = strip.frame_final_duration
    rand = a+int(random.random()*b)
    #print(a, a+b, rand)
    return rand


#
"""
def get_matching_markers(scene, name=None):
    '''return a list of markers with same name 
     from the scene, or all markers if name is None'''
    selected_markers=[]
    markers = scene.timeline_markers
    for mark in markers:
        #print(mark.name, name)
        if mark.name == name or name==None:
            selected_markers.append(mark.frame)
    return selected_markers


def generate_subsets_list(number_of_subsets):
    #generate marker subsets list
    subset_list = []
    subset_names = ['A','B','C','D','E','F']
    for subset in range(number_of_subsets):
        subset_list.append(subset_names[subset])
    return subset_list
"""

def get_marker_dict(scene, number_of_subsets):
    '''return a dict where: 
            keys = subset names
            values = list of markers'''
    #get markers from scene
    markers = scene.timeline_markers
    subset_list = generate_subsets_list(number_of_subsets)
    #generate dict with a list for each subset
    marker_dict = {}
    for subset in subset_list:
        list=get_matching_markers(scene, subset)
        marker_dict[subset] = list
    return marker_dict


def get_cut_dict(scene, number_of_subsets):
    '''return a dict where: 
            keys = markers in the scene + start and end
            values = duration in frames from key marker to next marker'''
    #generate cut_list
    
    list=get_matching_markers(scene)
    list.append(scene.frame_start)
    list.append(scene.frame_end)
    list.sort()
    #print("lista:",len(list),list)
    cut_dict ={}
    for i, j in enumerate(list):
        try:
            #print(j,list[i+1]-1-j)
            cut_dict[j] = list[i+1]-j
        except IndexError:
            continue  
    return cut_dict
    

def random_edit_from_random_subset(cut_dict, sources_dict):
    '''return a random edit from random subsets'''
    #generate subset list (strings)
    subset_list = generate_subsets_list(number_of_subsets)
    # copy sources_dict
    random_edit = []
    for cut in sorted(cut_dict.keys()):
        #escoge un subset al azar:   
        rand = random.randrange(number_of_subsets)
        subset = subset_list[rand]
        #check if source subset is empty
        print(len(sources_dict[subset]),subset)
        if len(sources_dict[subset]) == 0:
            sources_dict[subset] = get_matching_markers(selected_scene, subset)
            print("repeating "+ subset + " clips")
        marker = sources_dict[subset].pop()
        random_edit.append((cut, cut_dict[cut], subset, marker))
    return random_edit
