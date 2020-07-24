import cv2
import numpy as np
import imutils
img=cv2.imread('shapes.png',cv2.IMREAD_COLOR)
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,thresh=cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
contours=cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
contours=imutils.grab_contours(contours)
for cnt in contours:
	M=cv2.moments(cnt)
	cx=int(M["m10"]/M["m00"])
	cy=int(M["m01"]/M["m00"])
	peri=cv2.arcLength(cnt,True)
	approx=cv2.approxPolyDP(cnt,0.04*peri,True)
	cv2.drawContours(img,[cnt],0,(0,255,0),2)
	if len(approx)==3:
		shape='triangle'
	elif len(approx)==4:
		x,y,w,h=cv2.boundingRect(approx)
		if cv2.contourArea(cnt)==w*h:
			if w==h:
				shape='square'
			else:
				shape='rectangle'
		else:
			shape='diamond'
	else:
		(x,y),radius=cv2.minEnclosingCircle(cnt)
		if cv2.contourArea(cnt)==np.pi*radius*radius:
			shape='circle'
		else:
			shape='oval'
	cv2.putText(img,shape,(cx,cy),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,0),2)
cv2.imwrite('shapes_classified.png',img)
cv2.waitKey(0)
cv2.destroyAllWindows()