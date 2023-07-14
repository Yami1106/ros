#!/usr/bin/env python3 
import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from std_srvs.srv import Empty
from math import pi
 


def pose_callback(data):
    posx=data.x
    posy=data.y

    if posx<=0 or posx>=11 or posy<=0 or posy>=11:
        rospy.loginfo("the turtle is resetting please wait...")
        reset_turtle=rospy.ServiceProxy('/reset',Empty)
        reset_turtle()
        return True
    
    else:
        return False
        

def turtle_shapes():
    #all the shapes are regular 
    rospy.init_node("turtle_services")
    pub=rospy.Publisher('/turtle1/cmd_vel',Twist,queue_size=10)
    rate=rospy.Rate(1)
    shape=input("Enter the shape the turtle should make: ")
    if shape=='quadrilateral':
        vel=Twist()
        stop=Twist()
        while not rospy.is_shutdown():
            if (rospy.Subscriber('/turtle1/pose',Pose,pose_callback)==True):
                break

            else:
                rospy.sleep(1)
                side=int(input("Enter the side of quad: "))
                side=float(side)

                vel.linear.x=0.0
                vel.angular.z=0.0
                pub.publish(vel)
                rate.sleep()

                vel.linear.x = side
                vel.angular.z=0.0
                pub.publish(vel)
                rate.sleep()
                pub.publish(stop)
                rate.sleep()

                vel.linear.x=0.0
                vel.angular.z= pi/2
                pub.publish(vel)
                rate.sleep()
                pub.publish(stop)



    elif shape=='triangle':
        vel = Twist()
        stop = Twist()
        while not rospy.is_shutdown():
            if (rospy.Subscriber('/turtle1/pose',Pose,pose_callback)==True):
                break
            
            else:
                rospy.sleep(1)
                side= int(input("Enter the edge of the triangle :"))
                side=float(side)

                vel.linear.x=0.0
                vel.angular.z=0.0
                pub.publish(vel)
                rate.sleep()

                vel.linear.x = side
                vel.angular.z = 0.0
                pub.publish(vel)
                rate.sleep()
                pub.publish(stop)
                rate.sleep()

                vel.linear.x=0.0
                vel.angular.z=-2*pi/3
                pub.publish(vel)
                rate.sleep()
                pub.publish(stop)
                rate.sleep()



    elif shape == '5 pointer star':
        vel = Twist()
        stop = Twist()
        while not rospy.is_shutdown():
            if (rospy.Subscriber('/turtle1/pose',Pose,pose_callback)==True):
                break

            else:
                rospy.sleep(1)
                side= int(input("Enter the edge of the star :"))
                side=float(side)

                vel.linear.x=0.0
                vel.angular.z=0.0
                pub.publish(vel)
                rate.sleep()

                vel.linear.x = side
                vel.angular.z = 0.0
                pub.publish(vel)
                rate.sleep()
                pub.publish(stop)
                rate.sleep()


                rate.sleep()
                vel.linear.x=0.0
                vel.angular.z=-pi/5
                pub.publish(vel)
                rate.sleep()
                pub.publish(stop)
                rate.sleep()



                rate.sleep()
                vel.linear.x = side
                vel.angular.z = 0.0
                pub.publish(vel)
                rate.sleep()
                pub.publish(stop)
                rate.sleep()


                rate.sleep()
                vel.linear.x=0.0
                vel.angular.z=3*pi/5
                pub.publish(vel)
                rate.sleep()
                pub.publish(stop)
                rate.sleep()


            
if __name__=="__main__":
    turtle_shapes()



