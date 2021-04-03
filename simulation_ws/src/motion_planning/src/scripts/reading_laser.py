#! /usr/bin/env python

import rospy
from sensor_msgs.msg import LaserScan

def clbk_laser(msg):
	#720/5=144
	#dividing the range of the laser scan into 5 regions and logging the minimum distance of an obstacle from the robot in a region
	#this gives us 5 values instead of 720 points
	regions=[min(min(msg.ranges[0:143]),10),    #anything distance greater than 10 is considered infinity (because maximum range is 10 in m2wr.gazebo)
			 min(min(msg.ranges[144:257]),10),  #to get rid of that, we're using min(xxxx,10)
			 min(min(msg.ranges[288:431]),10),
			 min(min(msg.ranges[432:575]),10),
			 min(min(msg.ranges[576:713]),10)]
	rospy.loginfo(regions)

def main():
	rospy.init_node('reading_laser')

	sub=rospy.Subscriber('/m2wr/laser/scan',LaserScan,clbk_laser)	

	rospy.spin()

if __name__=='__main__':
	main()