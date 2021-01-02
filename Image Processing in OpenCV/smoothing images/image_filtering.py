import cv2 as cv
import numpy as np 
from matplotlib import pyplot as plt  

img = cv.imread('../../Pictures/opencv-logo-white.png')

# 2D Convoluution
# kernel = np.ones((5,5), np.float32)/25
# dst = cv.filter2D(img, -1, kernel)

# Averaging Blur
# blur = cv.blur(img, (5,5))

# Gaussian Blurring
blur = cv.GaussianBlur(img, (5,5), 0)

plt.subplot(121), plt.imshow(img), plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(blur), plt.title('Blurred')
plt.xticks([]), plt.yticks([])
plt.show()