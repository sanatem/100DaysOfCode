# Different visual efects on an image.
import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(1):

    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # BGR
    lower_blue = np.array([50,150,30])
    upper_blue = np.array([180,255,255])

    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    res = cv2.bitwise_and(frame,frame, mask= mask)

    kernel = np.ones((5,5),np.uint8)
    erosion = cv2.erode(mask,kernel,iterations = 1)
    dilation = cv2.dilate(mask,kernel,iterations = 1)

    # cv2.imshow('Original',frame)
    # cv2.imshow('Mask',mask)

    cv2.namedWindow('res',cv2.WINDOW_NORMAL)
    cv2.resizeWindow('res', 800,600)
    cv2.imshow('res',res)
    # cv2.imshow('Erosion',erosion)
    # cv2.imshow('Dilation',dilation)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()
