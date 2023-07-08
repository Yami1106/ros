#!/usr/bin/env python3 

import rospy
from std_msgs.msg import String

def command_callback(msg):
    rospy.loginfo("Received command: %s",msg.data)

def movement_sub():
    rospy.init_node('movement_subscriber')
    rospy.Subscriber('robot_commands',String,command_callback)
    rospy.spin()
if __name__=='__main__':
    movement_sub()
