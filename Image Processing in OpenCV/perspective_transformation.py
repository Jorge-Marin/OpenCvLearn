import cv2 as cv
import numpy as np
import matplotlib 
from matplotlib import pyplot as plt

img = cv.imread('../Pictures/sudoku.png')
rows, cols, ch = img.shape

pts1 = np.float32([[74,82],[492,70],[34,513],[517,518]])
pts2 = np.float32([[0,0],[300,0],[0,300],[300,300]])

M = cv.getPerspectiveTransform(pts1,pts2)

dst = cv.warpPerspective(img,M,(300,300))

plt.subplot(121),plt.imshow(img),plt.title('Input')
plt.subplot(122),plt.imshow(dst),plt.title('Output')
plt.show()