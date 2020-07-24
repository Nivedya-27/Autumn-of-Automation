import cv2 as cv
import numpy as np
import sys
import os
img=cv.imread('test.png')
if img is None:
	sys.exit('could not read the image; check directory')

grey=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
ret,bw=cv.threshold(grey,127,255,cv.THRESH_BINARY)
images=[grey,bw]
titles=['grayscale','black and white']
os.makedirs('bw_gray')
for i in range(2):
		cv.imwrite(os.path.join('bw_gray/',(titles[i]+'.png')),images[i])
if cv.waitKey(0)==27:
	cv.destroyAllWindows()