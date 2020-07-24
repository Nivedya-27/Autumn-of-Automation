import cv2 as cv
import numpy as np
import sys
img=cv.imread('test.png')
if img is None:
	sys.exit('could not read the image; check directory')

grey=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
ret,bw=cv.threshold(grey,127,255,cv.THRESH_BINARY)
images=[img,grey,bw]
titles=['original','grayscale','black and white']
for i in range(3):
	cv.imshow(titles[i],images[i])
cv.waitKey(0)
cv.destroyAllWindows()