import cv2
import numpy as np
img=cv2.imread('test.png',0)
laplacian=cv2.Laplacian(img,cv2.CV_64F)
cv2.imwrite('pencil_test.png',laplacian)