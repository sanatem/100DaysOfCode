# Training drawing different forms.
import numpy as np
import cv2

img = cv2.imread('../img/taecv.jpg',cv2.IMREAD_COLOR)

#OpenCV is BGR
# Line: img, from,to, of line, color,width
cv2.line(img,(0,0),(200,200),(0,0,255))
# Circle: img, pos, radius, color, fill the circle (-1)
cv2.circle(img,(200,200),55,(0,255,0))
# Rectangle: img, from, to, color.
cv2.rectangle(img,(10,10),(150,150),(255,0,0))

points = np.array([[10,5],[20,30],[15,60],[60,80]],np.int32)
# points = points.reshape(-1,-1,2)
# Points Img, array of points, connected?, color, line width
cv2.polylines(img,[points],False,(0,0,255),2)
# Text: img, text, pos, font, size, color, thickness,
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'Vamos los pi', (0,255), font, 1, (255,200,0),2)

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
