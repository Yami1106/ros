#!/usr/bin/env python3 

import rospy
from geometry_msgs.msg import Twist

def turtle_controller():
    rospy.init_node("turtle_control")
    pub=rospy.Publisher('/turtle1/cmd_vel',Twist,queue_size=12)
    rate=rospy.Rate(1)
    rate.sleep()

    for i in range (0,1):
        forward=Twist()
        forward.linear.x=-11.0
        pub.publish(forward)
        rospy.loginfo(forward)
if __name__=="__main__":
    turtle_controller()