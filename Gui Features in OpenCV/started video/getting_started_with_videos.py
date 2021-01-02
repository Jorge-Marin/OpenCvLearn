#Goals
    #Learn to read video, display video, and save video.
    #Learn to capture video from a camera and display it.
    #You will learn these functions : cv.VideoCapture(), cv.VideoWriter()

import cv2 as cv;
import numpy as np;

cap = cv.VideoCapture(0);

if not cap.isOpened(): #Verify if is initialized
    print("Cannot open camera");
    exit();

#cap.get(propId)  ids from 0 to 18
#cap.set(propId, value) Modify some values

while True:
    # Capture frame-by-frame
    ret, frame = cap.read();

    #if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting...");
        break;

    #Our operations on the frame come here
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY);
    # Display the resulting frame
    cv.imshow('frame', gray);
    if cv.waitKey(1) == ord("q"):
        break

#When everything done, release the capture.
cap.release();
cv.destroyAllWindows();