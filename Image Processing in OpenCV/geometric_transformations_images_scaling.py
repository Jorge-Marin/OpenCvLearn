import cv2 as cv
import numpy as np

img = cv.imread('../Pictures/messi5.jpg')

res = cv.resize(img, None, fx=2, fy=2, interpolation= cv.INTER_CUBIC)

#OR
height, width = img.shape[:2]
res = cv.resize(img, (2*width, 2*height), interpolation= cv.INTER_CUBIC)