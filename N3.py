#!/usr/bin/env python3 

import rospy
from std_msgs.msg import String

def node3_callback(msg):
    rospy.loginfo("Received message from N2: %s",msg.data)

def node3_subscriber():
    rospy.init_node("N3_sub")
    rospy.Subscriber("T2",String,node3_callback)
    rospy.spin()

if __name__=="__main__":
    node3_subscriber()
    