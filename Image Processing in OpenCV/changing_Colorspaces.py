import cv2 as cv
import numpy as np 

cap = cv.VideoCapture(1)

while(1):

    # Take each frame
    _, frame = cap.read()

    # Convert BGR to HSV
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    # Define range of red color in HSV
    lower_red = np.array([169,100,100])
    upper_red = np.array([189, 255, 255])

    # Define range of blue color in HSV
    lower_blue = np.array([110,50,50])
    upper_blue = np.array([130, 255, 255])

    # Define range of blue color in HSV
    lower_green = np.array([50,50,50])
    upper_green = np.array([70, 255, 255])

    # Threshold the HSV image to get only red colors
    mask_red = cv.inRange(hsv, lower_red, upper_red)
    mask_blue = cv.inRange(hsv, lower_blue, upper_blue)
    mask_green = cv.inRange(hsv, lower_green, upper_green)

    # Bitwise-AND mask and original image
    res_red = cv.bitwise_and(frame, frame, mask=mask_red)
    res_blue = cv.bitwise_and(frame, frame, mask=mask_blue)
    res_green = cv.bitwise_and(frame, frame, mask = mask_green)

    cv.imshow('frame', frame)
    cv.imshow('res_green', res_green)
    cv.imshow('res_red', res_red)
    cv.imshow('res_blue', res_blue)

    k = cv.waitKey(5) & 0xFF
    if k == 27:
        break

cv.destroyAllWindows()