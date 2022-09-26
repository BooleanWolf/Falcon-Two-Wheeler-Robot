#! /usr/bin/env python3


import rospy 
from geometry_msgs.msg import Twist 
from sensor_msgs.msg import LaserScan 
import time 



def main():
    rospy.init_node("cmd_control")
    msg = Twist()

    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)  
    linear_x = 0
    angular_z = 0
    while True:
        a = input()
        if a == "F":
            linear_x = 0.6
            angular_z = 0
        elif a == "B":
            linear_x = 0
            angular_z = 0.3
        elif a == "R":
            linear_x = 0
            angular_z = 0.3
        elif a == "L":
            linear_x = 0
            angular_z = -0.3
        else:
            break 
            
        msg.linear.x = -linear_x
        msg.angular.z = angular_z 
        pub.publish(msg)
        


if __name__ == '__main__':
    main()