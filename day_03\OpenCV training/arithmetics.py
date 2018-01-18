# Applying arithmetics on images.
import numpy as np
import cv2

tae = cv2.imread('img/taecv.jpg',cv2.IMREAD_COLOR)
tae_gray = cv2.cvtColor(tae,cv2.COLOR_BGR2GRAY)

yoona = cv2.imread('img/yoonacv.jpg', cv2.IMREAD_COLOR)

retval, threshold = cv2.threshold(tae, 125, 255, cv2.THRESH_BINARY)
retval, threshold_gray = cv2.threshold(tae_gray, 125, 255, cv2.THRESH_BINARY)
gaus = cv2.adaptiveThreshold(tae_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 5)
retval, otsu = cv2.threshold(tae_gray,125, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# Types of Add
# add = tae + yoona
# add = cv2.add(tae,yoona)
# weighted = cv2.addWeighted(tae,0.4,yoona,0.6,0)

cv2.imshow('original', tae)
cv2.imshow('threshold', threshold)
cv2.imshow('threshold_gray', threshold_gray)
cv2.imshow('threshold_GAUS', gaus)
cv2.imshow('threshold_otsu', otsu)

# cv2.imshow('image',add)
# cv2.imshow('weighted',weighted)

cv2.waitKey(0)
cv2.destroyAllWindows()
