#!/usr/bin/env python
import rospy
import math
from beginner_tutorials.msg import quaternion
from beginner_tutorials.msg import eulerangles
class my_converter(object):
	def __init__(self):
		self.angles=eulerangles()
		self.angles.yaw=0
		self.angles.pitch=0
		self.angles.roll=0
		rospy.init_node('my_converter',anonymous=True)
		rospy.Subscriber('topic1',quaternion,self.convert)
		self.pub=rospy.Publisher('topic2',eulerangles)

	def convert(self,msg):
		(x,y,z,w)=(msg.x,msg.y,msg.z,msg.w)
		self.angles.roll=math.atan2(2*y*w-2*x*z,1-2*y*y-2*z*z)
		self.angles.pitch=math.atan2(2*x*w-2*y*z,1-2*x*x-2*z*z)
		self.angles.yaw=math.asin(2*x*y+2*z*w)
	
	def run(self):
		r=rospy.Rate(10)
		while not rospy.is_shutdown():
			rospy.loginfo(self.angles)
			self.pub.publish(self.angles)
			r.sleep()

if __name__=='__main__':
	try:
		x=my_converter()
		x.run()
	except rospy.ROSInterruptException:
		pass