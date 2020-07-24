import cv2
import numpy as np
cap=cv2.VideoCapture('messi.webm')
while cap.isOpened():
	ret,frame=cap.read()
	output=frame.copy()
	gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	gray=cv2.medianBlur(gray,5)
	gray=cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,3.5)
	kernel=np.ones((3,3),np.uint8)
	gray=cv2.erode(gray,kernel,iterations=1)
	gray=cv2.dilate(gray,kernel,iterations=1)
	circles=cv2.HoughCircles(gray,cv2.HOUGH_GRADIENT,1,260,param1=30,param2=65,minRadius=0)
	radii=[]
	for (x,y,r) in circles:
		radii.append(r)
	R=max(radii)
	X=None
	Y=None
	for (x,y,r) in circles:
		if r==R:
			X=x
			Y=y
			break
	cv2.circle(output,(X,Y),R,(0,255,0),4)
	cv2.imshow('result',output)
	if cv.waitKey(0)==27:
		break
cap.release()
cv2.destroyAllWindows()