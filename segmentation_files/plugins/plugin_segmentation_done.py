#!/usr/bin/python
import time
import sys
import math
import gimp
from gimpfu import *
import os


def gprint( text ):
   pdb.gimp_message(text)
   return

def plugin_main(timg, tdrawable, maxh=500, maxw=500):

    gprint("DONE!!!!!")
    #filename="C:\Segmentation_files\\pic.jpg"
    #log code contour to file for progress
    with open('C:\\3d-Model\\bin\\segmentation_files\\progress.txt', 'w') as myFile:
            myFile.write("segment")
    os.chdir( 'C:\\3d-Model\\bin\\segmentation_files' )
    os.system( '"C:\\3d-Model\\bin\\segmentation_files\\squares_main.py"')
    pdb.gimp_quit(0)
    

register(
        "python_fu_segmentation_done",
        "DONE!!!!",
        "DONE!!!",
        "IIRS(ISRO),Dehradun",
        "2013",
        "<Image>/Segmentation/Crop all",
        "RGB*, GRAY*",
        [],[],
        plugin_main)

main()
