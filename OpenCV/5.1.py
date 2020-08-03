import cv2
import numpy as np
from imutils.video import FileVideoStream
import imutils
import time
vs = FileVideoStream('messi.webm').start()
while vs.more():
	frame=vs.read()
	if frame is None:
		continue
	output=frame.copy()
	gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	gray=cv2.medianBlur(gray,5)
	gray=cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,3,5)
	kernel=np.ones((3,3),np.uint8)
	gray=cv2.erode(gray,kernel,iterations=1)
	gray=cv2.dilate(gray,kernel,iterations=1)
	circles=cv2.HoughCircles(gray,cv2.HOUGH_GRADIENT,1,260,param1=30,param2=65,minRadius=0)
	radii=[]
	if circles is None:
		continue
	circles=np.uint16(np.around(circles))
	for i in range(circles.shape[0]):
		radii.append(circles[i][0][2])
	R=max(radii)
	X=None
	Y=None
	for i in range(circles.shape[0]):
		if circles[i][0][2]==R:
			X=circles[i][0][0]
			Y=circles[i][0][1]
			break
	cv2.circle(output,(X,Y),R,(0,255,0),4)
	cv2.imshow('result',output)
	cv2.waitKey(1)
cv2.destroyAllWindows()
vs.stop()