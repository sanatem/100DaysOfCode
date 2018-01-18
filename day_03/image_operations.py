# How to take a ROI (Region of Interest) or Mask from an image.
# And I also tested how to print a line/etc.
import numpy as np
import cv2

img = cv2.imread('img/taecv.jpg',cv2.IMREAD_COLOR)

# Image operations
px = img[55,55]
# We can print the color value
print(px)

# Draw a white pixel
# img[100:150,100:150] = [255,255,255]

# CV2 Line
#cv2.line(img,(0,0),(200,200),(0,0,255))

# Rectangle
#cv2.rectangle(img,(10,10),(150,150),(255,0,0))


# Region of image.
tae_face = img[37:180, 174:274]
# We copy-paste in another pixel.
img[0:143,0:100] = tae_face

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
