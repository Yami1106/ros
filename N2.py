#!/usr/bin/env python3 

import rospy
from std_msgs.msg import String

def node2_callback(msg):
    rospy.loginfo("Received message from N1: %s",msg.data)

def node2():
    rospy.init_node("N2")
    n2_sub=rospy.Subscriber('T1',String,node2_callback)
    n2_pub=rospy.Publisher('T2',String,queue_size=10)
    rate2=rospy.Rate(10)

    while not rospy.is_shutdown():
        msg2="Hi from N2"
        n2_pub.publish(msg2)
        rospy.loginfo(msg2)
        rate2.sleep()
if __name__=='__main__':
    node2()

