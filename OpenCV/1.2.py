import cv2 as cv
import numpy as np
cap=cv.VideoCapture(0)
if not cap.isOpened():
	raise IOError("cannot open webcam")

while True:
	ret,ip=cap.read()
	cv.imshow('video',ip)
	c=cv.waitKey(1)
	if c==27:#ASCII value of Esc key
		break #if Esc is pressed video stops

cap.release()
cv.destroyAllWindows()