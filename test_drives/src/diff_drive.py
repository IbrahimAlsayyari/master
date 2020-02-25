#! /user/bin/env python

import rospy
from geometry_msgs.msg import Twist
rospy.init_node("my_node")

pub = rospy.publisher("/robot/cmd_vel", Twist,queue.size=1)

vel = Twist()

vel.linear.x = 0.1


r =rospy.Rate(1)

while not rospy.is_shutdown():
    pub.publish(vel)
    r.sleep()