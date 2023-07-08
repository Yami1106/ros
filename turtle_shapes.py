#!/usr/bin/env python3 

import rospy
from geometry_msgs.msg import Twist
from math import pi

def turtle_controller():
    rospy.init_node("turtle_shapes")
    pub=rospy.Publisher('/turtle1/cmd_vel',Twist,queue_size=10)
    rate=rospy.Rate(1)
    shape=input("Enter the shape the turtle should make: ")
    if shape=='square':
        vel=Twist()
        stop=Twist()
        while not rospy.is_shutdown():
            vel.linear.x = 2.0
            vel.angular.z=0
            pub.publish(vel)
            rate.sleep()
            pub.publish(stop)
            rate.sleep()
            vel.linear.x=0
            vel.angular.z= pi/2
            pub.publish(vel)
            rate.sleep()
            pub.publish(stop)
    elif shape=='rectangle':
        vel = Twist()
        stop = Twist()
        while not rospy.is_shutdown():

            vel.linear.x = 2.0
            vel.angular.z = 0.0
            pub.publish(vel)
            rate.sleep()
            pub.publish(stop)
            rate.sleep()

            vel.linear.x = 0.0
            vel.angular.z = -pi/2
            pub.publish(vel)
            rate.sleep()
            pub.publish(stop)
            rate.sleep()

            vel.linear.x = 3.0
            vel.angular.z = 0.0
            pub.publish(vel)
            rate.sleep()
            pub.publish(stop)
            rate.sleep()

            vel.linear.x = 0.0
            vel.angular.z = -pi/2
            pub.publish(vel)
            rate.sleep()
            pub.publish(stop)
            rate.sleep()
    elif shape =='triangle':
        vel = Twist()
        stop = Twist()
        while not rospy.is_shutdown():
            vel.linear.x = 2.0
            vel.angular.z = 0.0
            pub.publish(vel)
            rate.sleep()
            pub.publish(stop)
            rate.sleep()

            vel.linear.x=0
            vel.angular.z=-2*pi/3
            pub.publish(vel)
            rate.sleep()
            pub.publish(stop)
            rate.sleep()

            vel.linear.x = 2.0
            vel.angular.z = 0.0
            pub.publish(vel)
            rate.sleep()
            pub.publish(stop)
            rate.sleep()

            vel.linear.x=0
            vel.angular.z=-2*pi/3
            pub.publish(vel)
            rate.sleep()
            pub.publish(stop)
            rate.sleep()
    elif shape == '5 pointer star':
        vel = Twist()
        stop = Twist()
        while not rospy.is_shutdown():
            vel.linear.x = 2.0
            vel.angular.z = 0.0
            pub.publish(vel)
            rate.sleep()
            pub.publish(stop)
            rate.sleep()

            vel.linear.x=0
            vel.angular.z=-pi/5
            pub.publish(vel)
            rate.sleep()
            pub.publish(stop)
            rate.sleep()

            vel.linear.x = 2.0
            vel.angular.z = 0.0
            pub.publish(vel)
            rate.sleep()
            pub.publish(stop)
            rate.sleep()

            vel.linear.x=0
            vel.angular.z=3*pi/5
            pub.publish(vel)
            rate.sleep()
            pub.publish(stop)
            rate.sleep()
    elif shape=='6 pointer star':
        vel = Twist()
        stop = Twist()
        while not rospy.is_shutdown():
            vel.linear.x = 1.0
            vel.angular.z = 0.0
            pub.publish(vel)
            rate.sleep()
            pub.publish(stop)
            rate.sleep()

            vel.linear.x=0
            vel.angular.z=-2*pi/3
            pub.publish(vel)
            rate.sleep()
            pub.publish(stop)
            rate.sleep()

            vel.linear.x = 1.0
            vel.angular.z = 0.0
            pub.publish(vel)
            rate.sleep()
            pub.publish(stop)
            rate.sleep()

            vel.linear.x=0
            vel.angular.z=pi/3
            pub.publish(vel)
            rate.sleep()
            pub.publish(stop)
            rate.sleep()
    else:
        rospy.loginfo("Invalid choose a shapr from the options")

              
if __name__=="__main__":
    turtle_controller()