import numpy as np;
import cv2 as cv;

cap = cv.VideoCapture('../Pictures/vtest.avi');

while cap.isOpened():
    ret, frame = cap.read();

    #if frame is read correcly ret is true
    if not ret:
        print("Can't receive frame (stream end?). Exiting...");
        break;

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY);

    cv.imshow("vtest", gray);
    if cv.waitKey(1) == ord('q'):
        break;

cap.release();
cv.destroyAllWindows();

