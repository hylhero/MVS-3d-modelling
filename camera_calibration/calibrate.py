import numpy as np
import cv2
import os
from common import splitfn

USAGE = '''
USAGE: calib.py [--save <filename>] [--debug <output path>] [--square_size] [<image mask>]
'''
if __name__ == '__main__':
    import sys, getopt
    from glob import glob
    count=1
    with open('C:\\3d-Model\\bin\\camera_calibration\\value.txt', 'w') as myFile:
            myFile.write("0")
    f = open("C:\\3d-Model\\bin\\camera_calibration\\path.txt","r")
                #Read whole file into data
    path=f.read()+"\\*.jpg"
    print path

    args, img_mask = getopt.getopt(sys.argv[1:], '', ['save=', 'debug=', 'square_size='])
    args = dict(args)
    try: img_mask = img_mask[0]
    except: img_mask = path
    img_names = glob(img_mask)
    debug_dir = args.get('--debug')
    square_size = float(args.get('--square_size', 1.0))

    pattern_size = (9, 6)
    pattern_points = np.zeros( (np.prod(pattern_size), 3), np.float32 )
    pattern_points[:,:2] = np.indices(pattern_size).T.reshape(-1, 2)
    pattern_points *= square_size

    obj_points = []
    img_points = []
    h, w = 0, 0
    for fn in img_names:
        print 'processing %s...' % fn,
        img = cv2.imread(fn, 0)
        h, w = img.shape[:2]
        found, corners = cv2.findChessboardCorners(img, pattern_size)
        if found:
            term = ( cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_COUNT, 30, 0.1 )
            cv2.cornerSubPix(img, corners, (5, 5), (-1, -1), term)
        if debug_dir:
            vis = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
            cv2.drawChessboardCorners(vis, pattern_size, corners, found)
            path, name, ext = splitfn(fn)
            cv2.imwrite('%s/%s_chess.bmp' % (debug_dir, name), vis)
        if not found:
            print 'chessboard not found'
            continue
        img_points.append(corners.reshape(-1, 2))
        obj_points.append(pattern_points)
        print 'ok'
        count=count+1
        print count
        with open('C:\\3d-Model\\bin\\camera_calibration\\value.txt', 'w') as myFile:
            myFile.write(str(count))

    rms, camera_matrix, dist_coefs, rvecs, tvecs = cv2.calibrateCamera(obj_points, img_points, (w, h))
    f = open(r"C:\3d-Model\bin\camera_calibration\sensor_value.txt","r")
                #Read whole file into data
    value=f.read()
    sensor_value=float(value)
    print sensor_value
    print type(sensor_value)
    print "RMS:", rms
    print "camera matrix:\n", camera_matrix
    print "distortion coefficients: ", dist_coefs.ravel()
    print "focal length:",(camera_matrix[0][0]*sensor_value)/3872
    with open('C:\\3d-Model\\bin\\camera_calibration\\calib_temp.txt', 'w') as myFile:
        myFile.write("Root Mean Square(RMS) value : "+str(rms)+"\n")
        myFile.write("Distortion Coefficients : ")
        for log in dist_coefs.ravel():
            myFile.write(str(log)+"\t")
        myFile.write("\n"+"Camera Matrix : "+"\n")
        for log in camera_matrix:
            myFile.write(str(log)+"\n")
        myFile.write("Focal Length : ")
        myFile.write(str((camera_matrix[0][0]*sensor_value)/3872)+"\n")

    with open('C:\\3d-Model\\bin\\camera_calibration\\finish.txt', 'w') as myFile:
        myFile.write("finish")
    cv2.destroyAllWindows()
    cv2.destroyAllWindows()

