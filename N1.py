#!/usr/bin/env python3 

import rospy
from std_msgs.msg import String

def node1_pub():
    rospy.init_node("N1_pub")
    n1_pub=rospy.Publisher('T1',String,queue_size=10)
    rate1 = rospy.Rate(10)

    while not rospy.is_shutdown():
        msg1="Hi from N1"
        n1_pub.publish(msg1)
        rospy.loginfo(msg1)
        rate1.sleep()

if __name__=='__main__':
    node1_pub()


