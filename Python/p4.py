import numpy as np
X=np.random.normal(5,0.01,size=(20,20))
y=[]
try:
	print("enter values for y or press ctrl-C to get random array instead")
	for i in range(20):
		p=int(input(str(i)+'. '))
		y.append(p)
	y=np.array(y,dtype=np.int32)
except KeyboardInterrupt:
	y=np.random.randint(0,100,size=20,dtype=np.int32)
y=y.reshape((20,1))
theta=np.dot(np.dot(np.linalg.inv(np.dot(X.T,X)),X.T),y)
print(theta)