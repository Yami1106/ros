#!/usr/bin/env python3 

import rospy
from geometry_msgs.msg import Twist

def turtle_controller():
    rospy.init_node("turtle_control")
    pub=rospy.Publisher('/turtle1/cmd_vel',Twist,queue_size=10)
    rate=rospy.Rate(1)

    while not rospy.is_shutdown():
        forward=Twist()
        forward.linear.x=1.0
        pub.publish(forward)
        rospy.loginfo("moving forward")

        rate.sleep()

        stop=Twist()
        pub.publish(stop)
        rospy.loginfo("stop")

        rate.sleep()

        rotate=Twist()
        rotate.angular.z=1.0
        pub.publish(rotate)
        rospy.loginfo("rotating")
        
        rate.sleep()

        pub.publish(stop)
        rospy.loginfo("stop")

        rate.sleep()

if __name__== '__main__':
    turtle_controller()



