import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while 1:
  _,frame = cap.read()

  # Code goes here
  # Different filters to edge detection:
  # Laplacian filter
  laplacian = cv2.Laplacian(frame,cv2.CV_64F)
  # Sobel in X
  sobelx = cv2.Sobel(frame,cv2.CV_64F, 1, 0, ksize = 5)
  # Sobel in Y
  sobely = cv2.Sobel(frame,cv2.CV_64F, 0, 1, ksize = 5)

  # Edge detectors
  edges = cv2.Canny(frame,100,100)
  #cv2.imshow('laplacian',laplacian)
  #cv2.imshow('sobelx',sobelx)
  #cv2.imshow('sobely',sobely)
  cv2.imshow('canny', edges)

  if cv2.waitKey(1) & 0xFF == ord('q'):
    break

cv2.destroyAllWindows()
cap.release()
