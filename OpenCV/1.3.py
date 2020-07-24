import cv2 as cv
import numpy as np
import sys
bgr=cv.imread('test.png')
if bgr is None:
	sys.exit('could not open image')
rgb=cv.cvtColor(bgr,cv.COLOR_BGR2RGB)
img=bgr.copy()
img[:,:,2]=0
img[:,:,0]=img[:,:,0]+rgb[:,:,0]
cv.imwrite('converted.png',img)
if cv.waitKey(0)==27:
	cv.destroyAllWindows()