# Gaus and otsu algorithms test.
import cv2
import numpy as np

# Capturing device
cap = cv2.VideoCapture(0)

while True:
  ret,frame = cap.read()

  gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

  gaus = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 5)
# retval, otsu = cv2.threshold(gray,125, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

  cv2.imshow('gray',gaus)

  if cv2.waitKey(1) & 0xFF == ord('q'):
    break

cap.release()
cv2.destroyAllWindows()
