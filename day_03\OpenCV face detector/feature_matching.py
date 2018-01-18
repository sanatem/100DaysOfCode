# Feature matching from an image.
import cv2
import numpy as np
import matplotlib.pyplot as plt
# Homography - Brute force

template = cv2.imread('img/bag.jpg', 1)
feature = cv2.imread('img/bear.jpg', 1)
# ORB (Oriented FAST and Rotated BRIEF) is a detector of features
orb = cv2.ORB_create()

# Find keypoints and descriptors of the images
kp1, des1 = orb.detectAndCompute(template, None)
kp2, des2 = orb.detectAndCompute(feature, None)

# Brute force feature matcher
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck = True)

# Matching and ordering
matches = bf.match(des1, des2)
matches = sorted(matches, key = lambda x:x.distance)

# Plot the results
result = cv2.drawMatches(template, kp1, feature, kp2, matches[:10], None, flags = 2)

plt.imshow(result)
plt.show()
