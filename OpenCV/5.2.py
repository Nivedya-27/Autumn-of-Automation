import cv2
import numpy as np
from imutils.video import FileVideoStream
vs=FileVideoStream('messi.webm').start()
ball=cv2.imread('ball.png')
Ball=ball.copy()
ball=cv2.cvtColor(ball,cv2.COLOR_BGR2GRAY)
ball=cv2.medianBlur(ball,5)
ball=cv2.adaptiveThreshold(ball,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,3,5)
while vs.more():
	frame=vs.read()
	if frame is None:
		continue
	output=frame.copy()
	frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	frame=cv2.medianBlur(frame,5)
	frame=cv2.adaptiveThreshold(frame,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,3,5)
	if frame is None:
		continue
	orb=cv2.ORB_create()
	kp1,des1=orb.detectAndCompute(ball,None)
	kp2,des2=orb.detectAndCompute(frame,None)
	bf=cv2.BFMatcher(cv2.NORM_HAMMING,crossCheck=True)
	if des1 is None or des2 is None:
		continue
	matches=bf.match(des1,des2)
	matches=sorted(matches,key=lambda x:x.distance)
	img=cv2.drawMatches(Ball,kp1,output,kp2,matches[:10],flags=2,outImg=output)
	cv2.imshow('result',img)
	cv2.waitKey(1)
cv2.destroyAllWindows()
vs.stop()