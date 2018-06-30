import sys
import cv2
import cv2.cv as cv
import Image
import os
import wx
import subprocess

# some default constants
_SIZE = 800
_DEFAULT_LEVEL= 3
win_name = "Canny Edge"
trackbar_name = "Threshold"
# definition of some colors
_red =  (0, 0, 255, 0);
_green =  (0, 255, 0, 0);
_white = (255,255,255,0)
_black = (0,0,0,0)
startSvgTag = """<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN"
"http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">
<svg version="1.1"
xmlns="http://www.w3.org/2000/svg"
xmlns:xlink="http://www.w3.org/1999/xlink"
width="240px" height="240px" viewBox="0 0 240 240">"""
endSvgTag = """</svg>"""

def get_path():
    
    f = open("C:\\3d-Model\\bin\\segmentation_files\\path.txt","r")
    #Read whole file into data
    path = f.read()
    print path
    return path

def on_contour(position):
    # compute the real level of display, given the current position
    levels = position-3

    # initialisation
    _contours = contours

    if levels <= 0:
        # zero or negative value
        # => get to the nearest face to make it look more funny
        _contours = contours.h_next().h_next().h_next()

    # first, clear the image where we will draw contours
    cv.SetZero (contours_image)

    # draw contours in red and green
    cv.DrawContours (contours_image, _contours,_white, _green,levels, 1, cv.CV_AA,(0, 0))

    # finally, show the image
    cv.ShowImage ("contours", contours_image)
    
def on_trackbar(position):

    cv.Smooth(gray, edge, cv.CV_BLUR, 3, 3, 0)
    cv.Not(gray, edge)

    # run the edge dector on gray scale
    cv.Canny(gray, edge, position, position * 3, 3)

    # reset
    cv.SetZero(col_edge)

    # copy edge points
    cv.Copy(im, col_edge, edge)

    # show the im
    cv.ShowImage(win_name, col_edge)

    


if __name__ == '__main__':

    #select picture from the computer path is same as selected in gui
    select_pic=get_path()

    #read image
    img = cv2.imread(select_pic)

    #save the clone image for square_main in segmentation_files
    image_clone = Image.open(select_pic)
    image_clone.save("C:\\3d-Model\\bin\\segmentation_files\\pic.jpg")
    print "Clone created"
    
    
    #perform gaussian blur
    Gaussian_Blur = cv2.GaussianBlur(img,(25,25),0)
    img=Image.fromarray(Gaussian_Blur)
    img.save("C:\\3d-Model\\bin\\segmentation_files\\pic_blur.jpg")

    im = cv.LoadImage("C:\\3d-Model\\bin\\segmentation_files\\pic_blur.jpg",cv.CV_LOAD_IMAGE_COLOR)
    #create the output image for canny
    col_edge = cv.CreateImage((im.width, im.height), 8, 3)
    # create the image for putting in it the founded contours
    contours_image = cv.CreateImage ( (im.width, im.height) ,8, 3)

    print type(col_edge)
    print im.width

    # convert to grayscale for canny
    gray = cv.CreateImage((im.width, im.height), 8, 1)
    edge = cv.CreateImage((im.width, im.height), 8, 1)
    cv.CvtColor(im, gray, cv.CV_BGR2GRAY)

    # create the window for canny edge
    cv.NamedWindow(win_name, cv.CV_WINDOW_NORMAL)
  
    
    # create the trackbar for canny
    cv.CreateTrackbar(trackbar_name, win_name, 1, 40, on_trackbar)

    # show the canny image
    on_trackbar(0)

    # wait a key pressed to end and open contour code
    cv.WaitKey(0)
    cv.SaveImage('C:\\3d-Model\\bin\\segmentation_files\\pic_seg.jpg', col_edge) # save the image as jpg
    #save the image as svg
    #files="C:\\3d-Model\\bin\\segmentation_files\\pic_seg.jpg"
    #pngFile = open(files, 'rb')
    #base64data = pngFile.read().encode("base64").replace('\n','')
    #base64String = '<image xlink:href="data:image/png;base64,{0}" width="im.width" height="im.height" x="0" y="0" />'.format(base64data)

    #f = open(os.path.splitext(files)[0]+".svg",'w')
    #f.write( startSvgTag + base64String + endSvgTag)
    #print 'Converted '+ files + ' to ' + os.path.splitext(files)[0]+".svg"

    #log code canny to file for progress
    with open('C:\\3d-Model\\bin\\segmentation_files\\progress.txt', 'w') as myFile:
            myFile.write("canny")
    
    #CONTOUR  MAKING CODE

    # create the image where we want to display results
    image = cv.CreateImage ( (_SIZE, _SIZE), 8, 1)

    # start with an empty image
    cv.SetZero (image)


    im = cv.LoadImage("C:\\3d-Model\\bin\\segmentation_files\\pic_seg.jpg", cv.CV_LOAD_IMAGE_COLOR)
    image = cv.CreateImage((im.width, im.height), 8, 1)
    cv.CvtColor(im, image, cv.CV_BGR2GRAY)
    threshold=51
    colour=255
    cv.Threshold(image,image, threshold,colour,cv.CV_THRESH_BINARY)

    # create the window for the contours
    cv.NamedWindow ("contours", cv.CV_WINDOW_NORMAL)

    # create the trackbar, to enable the change of the displayed level
    cv.CreateTrackbar ("levels+3", "contours", 3, 7, on_contour)

    # create the storage area for contour image
    storage = cv.CreateMemStorage (0)

    # find the contours
    contours = cv.FindContours(image,storage,cv.CV_RETR_TREE,cv.CV_CHAIN_APPROX_SIMPLE,(0,0))

    # polygon approxomation 
    contours = cv.ApproxPoly(contours,storage,cv.CV_POLY_APPROX_DP, 3, 1)

    # call one time the callback, so we will have the 1st display of contour window
    on_contour (_DEFAULT_LEVEL)

    cv.WaitKey (0)
    cv.SaveImage('C:\\3d-Model\\bin\\segmentation_files\\pic_contours.jpg', contours_image) # save the image as png
    cv.DestroyAllWindows()

    #log code contour to file for progress
    with open('C:\\3d-Model\\bin\\segmentation_files\\progress.txt', 'w') as myFile:
            myFile.write("contour")

    #open gimp after end of thresholding and contour
    os.chdir( 'C:\\Program Files\\GIMP 2\\bin' )
    os.system( '"C:\\Program Files\\GIMP 2\\bin\\gimp-2.8.exe"')
    

    

