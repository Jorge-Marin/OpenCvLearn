import cv2 as cv
import numpy as np 
from matplotlib import pyplot as plt

img = cv.imread('../../Pictures/j.png')
kernel = np.ones((5,5), np.uint8)
erosion = cv.erode(img, kernel, iterations=1)

# Dilation
dilation = cv.dilate(img, kernel, iterations=1)

# Opening removing noise
opening = cv.morphologyEx(img, cv.MORPH_OPEN, kernel)

# Closing
closing = cv.morphologyEx(img, cv.MORPH_CLOSE, kernel)

# Morphological Gradient
gradient = cv.morphologyEx(img, cv.MORPH_GRADIENT, kernel)

plt.subplot(111), plt.imshow(img), plt.title('Original')
plt.subplot(112), plt.imshow(erosion), plt.title('Erosion')
plt.show()