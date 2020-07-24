import cv2 as cv
import numpy as np
import sys
img=cv.imread('test.png')
if img is None:
	sys.exit('could not open image')
new=cv.cvtColor(img,cv.COLOR_BGR2RGB)
cv.imshow('converted',new)
cv.waitKey(0)
cv.destroyAllWindows()