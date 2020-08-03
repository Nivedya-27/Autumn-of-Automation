import cv2
import numpy as np

def detect(c):
	perimeter=cv2.arcLength(c,True)
	approx=cv2.approxPolyDP(c,0.04*perimeter,True)
	if len(approx)==3:
		return 'triangle'
	if len(approx)==4:
		x,y,w,h=cv2.boundingRect(approx)
		#if cv2.contourArea(c)==w*h:
		if w/float(h)<=1.05 and w/float(h)>=0.95:
			return 'square'
		return 'rectangle'
	(x,y),radius=cv2.minEnclosingCircle(c)
	if abs(cv2.contourArea(c)-np.pi*(radius**2))<=0.5:
		return 'circle'
	return 'oval'

img=cv2.imread('shapes1.jpg',cv2.IMREAD_COLOR)
img=cv2.bilateralFilter(img,9,75,75)
#cv2.imwrite('filtered.png',img)
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,thresh2=cv2.threshold(gray,127,255,cv2.THRESH_BINARY_INV)
#cv2.imwrite('bw.png',thresh2)
_,contours,hierarchy=cv2.findContours(thresh2,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
#print(len(contours))
for cnt in contours:
	M=cv2.moments(cnt)
	cx=int((M["m10"]/M["m00"]))
	cy=int((M["m01"]/M["m00"]))
	shape=detect(cnt)
	img=cv2.putText(img,shape,(cx,cy),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,0),2)
#cv2.imwrite('shapes_classified.png',img)
cv2.imshow('classified',img)
if cv2.waitKey(0)==27:
	cv2.destroyAllWindows()