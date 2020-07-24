import cv2
import numpy
cap=cv2.VideoCapture(0)
if not cap.isOpened():
	raise IOError("unable to open Webcam")
while True:
	ret,frame=cap.read()
	lapl=cv2.Laplacian(frame,cv2.CV_64F)
	cv2.imshow('pencil',lapl)
	c=cv2.waitKey(1)
	if c==27:
		break
cap.release()
cv2.destroyAllWindows()