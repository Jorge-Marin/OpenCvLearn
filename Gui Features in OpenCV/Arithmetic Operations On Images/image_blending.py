import cv2 as cv
import numpy as np 

img1 = cv.imread('../Pictures/Blender_Suzanne1.jpg')
img2 = cv.imread('../Pictures/Blender_Suzanne2.jpg')

print(img1.size)
print(img2.size)
dst = cv.addWeighted(img1, 0.7, img2, 0.5,0)

cv.imshow('dst', dst)
cv.waitKey(0)
cv.destroyAllWindows()