#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
pi=3.141592

def straight(d,vel_msg,pub):
	vel_msg.linear.x=2
	t0=rospy.Time.now().to_sec()
	traveled=0
	while(traveled<d):
		pub.publish(vel_msg)
		t1=rospy.Time.now().to_sec()
		traveled=2*(t1-t0)
	vel_msg.linear.x=0
	pub.publish(vel_msg)

def rotate(angle,vel_msg,pub):
	if angle>=0:#anticlockwise
		vel_msg.angular.z=1.8
	else:
		vel_msg.angular.z=-1.8
	angle=abs(angle)
	t0=rospy.Time.now().to_sec()
	steered=0
	while steered<angle:
		pub.publish(vel_msg)
		t1=rospy.Time.now().to_sec()
		steered=1.8*(t1-t0)
	vel_msg.angular.z=0
	pub.publish(vel_msg)

def draw():
	rospy.init_node('my_initials',anonymous=True)
	pub=rospy.Publisher('/turtle1/cmd_vel',Twist,queue_size=10)
	vel_msg=Twist()
	vel_msg.linear.x=0
	vel_msg.linear.y=0
	vel_msg.linear.z=0
	vel_msg.angular.x=0
	vel_msg.angular.y=0
	vel_msg.angular.z=0
	while not rospy.is_shutdown():
		rotate(pi/float(2),vel_msg,pub)
		straight(3,vel_msg,pub)
		angle=-(127*pi)/180
		rotate(angle,vel_msg,pub)
		straight(5,vel_msg,pub)
		rotate(-angle,vel_msg,pub)
		straight(3,vel_msg,pub)
	rospy.spin()


if __name__=='__main__':
	try:
		draw()
	except rospy.ROSInterruptException:
		pass
