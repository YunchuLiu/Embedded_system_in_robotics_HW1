#!/usr/bin/env python
import rospy
from math import *


#call the service to locate the turtle
from turtlesim.srv import TeleportAbsolute
from geometry_msgs.msg import Twist


def publish_velocity():
    pub=rospy.Publisher('/turtle1/cmd_vel',Twist,queue_size=10)
    rospy.init_node('publish_velocity', anonymous=True)
    rate=rospy.Rate(10)
    
    base_time=rospy.get_time()
    
    while not rospy.is_shutdown():
        T=10
        t=rospy.get_time()-base_time
        msg=Twist()
        dx=12*pi/T*cos(4*pi*t/T)
        dy=6*pi/T*cos(2*pi*t/T)
        dx2 = -48*pi*pi*sin((4*pi*t)/T)/(T*T)
        dy2 = -12*pi*pi*sin((2*pi*t)/T)/(T*T)
        msg.linear.x=dx
        msg.linear.y=dy
        msg.linear.z=0
        msg.angular.x=0
        msg.angular.y=0
        msg.angular.z=0
        pub.publish(msg)
        rate.sleep()
    
        
def locate_the_turtle_client(x,y,theta):
    rospy.wait_for_service('/turtle1/teleport_absolute')
    try:
        locate_the_turtle=rospy.ServiceProxy('/turtle1/teleport_absolute',TeleportAbsolute)
        locate_the_turtle(x,y,theta)
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e
        
def main():
    locate_the_turtle_client(5.45,5.45,0)
    publish_velocity()
        
main()


     
    
    


