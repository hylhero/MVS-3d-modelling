#!/usr/bin/python
import time
import sys
import math
import gimp
from gimpfu import *
from os.path import join
import os


# create an output function that redirects to gimp's Error Console
def gprint( text ):
   pdb.gimp_message(text)
   return

def plugin_main(image, __unused_drawable, name_pattern):

    gprint("ADD NEW LAYER...")
    #save previous layer
    layer=image.layers[0]
    directory="C:\\3d-Model\\bin\\segmentation_files"
    filename = join(directory, name_pattern)
    print type(name_pattern)
    
    raw_filename = name_pattern
    text_file=raw_filename[:raw_filename.find(".")]+".txt"
    
    with open("C:\\3d-Model\\bin\\segmentation_files\\seg_text.txt", 'w') as myFile:
            myFile.write(str(text_file))
    pdb.gimp_file_save(image, layer, filename, raw_filename)
    #upgrade database
    os.chdir( 'C:\\3d-Model\\bin\\segmentation_files' )
    os.system( '"C:\\3d-Model\\bin\\segmentation_files\\GUI.py"')
    #add new layer
    image = gimp.image_list()[0]
    layer=image.layers[0]
    layer = pdb.gimp_layer_new(image, image.width, image.height, 1, "segmented contours", 100, 0)
    image.add_layer(layer, -1)
    
    
    
register(
        "python_fu_segmentation_savelayer",
        "save a segment and load a new layer",
        "save a segment and load a new layer",
        "IIRS(ISRO),Dehradun",
        "2013",
        "<Image>/Segmentation/Save Segment",
        "*",
        [
        #(PF_DIRNAME, "directory", "Directory to put the images on", "/"),
        (PF_STRING, "name_pattern", "Pattern for file name, %s will be replaced with layer name", ".png"),
        ],
        [],
        plugin_main
        )

main()
