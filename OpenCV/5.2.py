import cv2
import numpy as np
cap=cv2.VideoCapture('messi.webm')
ball=cv2.imread('ball.png')
ball=cv2.cvtColor(ball,cv2.COLOR_BGR2GRAY)
ball=cv2.medianBlur(ball,5)
while cap.isOpened():
	ret,frame=cap.read()
	frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	frame=cv2.medianBlur(frame,5)
	orb=cv2.ORB()
	kp1,des1=orb.detectAndCompute(ball,None)
	kp2,des2=orb.detectAndCompute(frame,None)
	bf=cv2.BFMatcher(cv2.NORTH_HAMMING,crossCheck=True)
	matches=bf.match(des1,des2)
	matches=sorted(matches,key=lambda x:x.distance)
	img=cv2.drawMatches(ball,kp1,frame,kp2,matches[:10],flags=2)
	cv2.imshow(img)
	if cv2.waitKey(0)==27:
		break
cap.release()
cv2.destroyAllWindows()