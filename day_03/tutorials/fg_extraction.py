# Foreground extraction from an image.
import cv2
import numpy as np
import matplotlib.pyplot as plt # Library for plotting.

img = cv2.imread('img/taecv.jpg')
mask = np.zeros(img.shape[:2], np.uint8)

bgModel = np.zeros((1,65), np.float64)
fgModel = np.zeros((1,65), np.float64)

rect = (50, 20, 350, 500)

cv2.grabCut(img, mask, rect, bgModel, fgModel, 5, cv2.GC_INIT_WITH_RECT)

new_mask = np.where( (mask==2) | (mask==0), 0, 1).astype('uint8')
img = img*new_mask[:,:,np.newaxis]

plt.imshow(img)
plt.colorbar()
plt.show()
