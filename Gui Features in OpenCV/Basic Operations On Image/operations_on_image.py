import numpy as np
import cv2 as cv

img = cv.imread('../Pictures/messi5.jpg');

px = img[100,100]
print(px);

# accessing olny blue pixel

blue = img[100,100,0]
print(blue)

# modify pixel value
img[100,100] = [255,255,255]
print(img[100,100])

#accesing red value
print(img.item(10,10,2))

#modify red value
img.itemset((10,10,2), 100)
print(img.item(10,10,2))

print(img.shape)
print(img.size)
print(img.dtype)

ball = img[280:340,330:390]
img[273:333, 100:160] = ball
b, g, r = cv.split(img)
img = cv.merge((b, g, r))

cv.imshow('messi', img)
cv.waitKey(0)
cv.destroyAllWindows();

