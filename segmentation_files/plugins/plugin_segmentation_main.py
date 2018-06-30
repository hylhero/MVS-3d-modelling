#!/usr/bin/python
import time
import sys
import math
import gimp
from gimpfu import *

opacity=70
brush_size=15.0
# create an output function that redirects to gimp's Error Console
def gprint( text ):
   pdb.gimp_message(text)
   return

def plugin_main(timg, tdrawable, maxh=500, maxw=500):

    gprint("Layering tool...")
    filename="C:\\3d-Model\\bin\\segmentation_files\\pic.jpg"
    image = pdb.file_jpeg_load(filename, filename)
    #image = gimp.image_list()[0]
    display = pdb.gimp_display_new(image)
    loaded_layer = pdb.gimp_file_load_layer(image,"C:\\3d-Model\\bin\\segmentation_files\\pic_contours.jpg")
    pdb.gimp_layer_set_opacity(loaded_layer, opacity)
    image.add_layer(loaded_layer, -1)
    layer = pdb.gimp_layer_new(image, image.width, image.height, 1, "segmented contours", 100, 0)
    image.add_layer(layer, -2)
    pdb.gimp_context_set_brush_size(brush_size)
    
    
register(
        "python_fu_segmentation",
        "create layering tool for manual noise correction",
        "create layering tool for manual noise correction",
        "IIRS(ISRO),Dehradun",
        "2013",
        "<Image>/Segmentation/Open Project",
        "RGB*, GRAY*",
        [],[],
        plugin_main)

main()
