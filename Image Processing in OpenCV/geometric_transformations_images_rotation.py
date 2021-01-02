import cv2 as cv
import numpy as np

img = cv.imread('../Pictures/messi5.jpg', 0)
rows, cols = img.shape

# cols-1 and rows-1 are the coordinate limits
M = cv.getRotationMatrix2D(((cols-1)/2.0, (rows-1)/2.0),45,1)
dst = cv.warpAffine(img, M, (cols, rows))

cv.imshow('rotation', dst)
cv.waitKey(0)
cv.destroyAllWindows()