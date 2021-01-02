import cv2 as cv; #Import OpenCv Library
import sys;
import os;

#Reading the picture
img = cv.imread("../Pictures/starry_night.jpg");

#Exception control
if img is None:
    sys.exit("Could no read the image");

#Show Image, Windows Names , cv.Mat object
cv.imshow("Display window", img);
k = cv.waitKey(0); #Recive  letter

#save copy picture
if k == ord("s"):
    directory = r'C:\Users\jorge\Documents\OPENCV Projects\started image';
    os.chdir(directory);
    cv.imwrite("starry_night.png", img)
