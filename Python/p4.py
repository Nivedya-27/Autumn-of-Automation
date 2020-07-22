import numpy as np
X=np.random.normal(5,0.01,size=(20,20)) #X has numbers centred around 5 with std deviation 0.01
y=np.random.randint(0,100,size=20,dtype=np.int32) #y has random integers between 0 and 100
y=y.reshape((20,1)) # to enable standard matrix multipication
theta=np.dot(np.dot(np.linalg.inv(np.dot(X.T,X)),X.T),y) #the formula specified
print(theta)