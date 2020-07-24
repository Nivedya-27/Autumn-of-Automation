import cv2
import numpy as np
import os
img=cv2.imread('SS.png',0)
rows,cols=img.shape
os.makedirs('Augmented-imgs')
for i in range(4):
	M=np.float32([[1,0,100*i-150],[0,1,50]])
	dst=cv2.warpAffine(img,M,(cols,rows))
	cv2.imwrite(os.path.join('Augmented-imgs/',('translate'+str(i+1)+'.png')),dst)
	R=cv2.getRotationMatrix2D((cols/2,rows/2),60*i-90,1)
	dst=cv2.warpAffine(img,R,(cols,rows))
	cv2.imwrite(os.path.join('Augmented-imgs/',('rotate'+str(i+1)+'.png')),dst)
	if i==0:
		blur=cv2.blur(img,(5,5))
		cv2.imwrite(os.path.join('Augmented-imgs/'+('blur'+str(i+1)+'.png')),blur)
	if i==1:
		blur=cv2.medianBlur(img,5)
		cv2.imwrite(os.path.join('Augmented-imgs/'+('blur'+str(i+1)+'.png')),blur)