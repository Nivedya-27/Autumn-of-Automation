import cv2
import numpy as np
import os
img=cv2.imread('shapes.png',cv2.IMREAD_COLOR)
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,thresh=cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
all_contours,hierarchy=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
contours=[]
for cnt in all_contours:
	if cv2.isContourConvex(cnt):
		contours.append(cnt)
shape={}
os.makedirs('shape_rec')
for cnt in contours:
	area=cv2.contourArea(cnt)
	x,y,w,h=cv2.boundingRect(cnt)
	i=contours.index(cnt)
	if area==w*h:
		if w==h:
			shape[i]='square'
		else:
			shape[i]='rectangle'
	else:
		(x,y),r=cv2.minEnclosingCircle(cnt)
		if area==np.pi*r*r:
			shape[i]='circle'
		else:
			try:
				if cv2.fitEllipse(cnt)==cv2.minAreaRect(cnt):
					shape[i]='oval'
			except:
				if r==max(w/2,h/2):
					shape[i]='diamond'
				else:
					shape[i]='triangle'
	im=np.zeros(img.shape)
	cv2.drawContours(im,[cnt],0,(0,255,0),3)
	cv2.imwrite(os.path.join('shape_rec/'+(shape[contours.index(cnt)]+'.png')),im)