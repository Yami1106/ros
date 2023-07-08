#!/usr/bin/env python3 

import rospy 
from std_msgs.msg import String

def sense_pub():
    rospy.init_node('sensor_publisher')

    pub= rospy.Publisher('robot_commands',String,queue_size=14)
    rate=rospy.Rate(14)

    while not rospy.is_shutdown():
        data="Can move"
        pub.publish(data)
        rospy.loginfo(data)
        rate.sleep()

if __name__=='__main__':
    sense_pub()