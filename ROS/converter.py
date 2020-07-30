import rospy
import math
from quaternion.msg import quaternion
from rpy.msg import eulerangles
class my_converter(object):
	def __init__(self):
		self.angles=(0.0,0.0,0.0)
		#self.value=(self.yaw,self.pitch,self.roll)
		rospy.init_node('my_converter',anonymous=True)
		rospy.Subscriber('topic1',quaternion,self.convert)
		self.pub=rospy.Publisher('topic2',eulerangles)

	def convert(self,msg):
		(x,y,z,w)=msg.data
		self.roll=math.atan2(2*y*w-2*x*z,1-2*y*y-2*z*z)
		self.pitch=math.atan2(2*x*w-2*y*z,1-2*x*x-2*z*z)
		self.yaw=math.asin(2*x*y+2*z*w)
		self.angles=(self.yaw,self.pitch,self.roll)
	
	def run(self):
		r=rospy.Rate(10)
		while not rospy.is_shutdown():
			rospy.loginfo(angles)
			self.pub.publish(self.angles)
			r.sleep()

if __name__=='__main__':
	try:
		x=my_converter()
		x.run()
	except rospy.ROSInterruptException:
		pass