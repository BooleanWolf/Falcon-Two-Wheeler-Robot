#! /usr/bin/env python3

import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist, Point
from nav_msgs.msg import Odometry
from tf import transformations

import math , time 



# nav_msgs/Odometry]:
# std_msgs/Header header
#   uint32 seq
#   time stamp
#   string frame_id
# string child_frame_id
# geometry_msgs/PoseWithCovariance pose
#   geometry_msgs/Pose pose
#     geometry_msgs/Point position
#       float64 x
#       float64 y
#       float64 z
#     geometry_msgs/Quaternion orientation
#       float64 x
#       float64 y
#      float64 z
#       float64 w
#   float64[36] covariance
# geometry_msgs/TwistWithCovariance twist
#   geometry_msgs/Twist twist
#     geometry_msgs/Vector3 linear
#       float64 x
#       float64 y
#       float64 z
#     geometry_msgs/Vector3 angular
#       float64 x
#       float64 y
#       float64 z
#   float64[36] covariance



def callback_odom(msg):
    global position 
    global yaw 

    position = msg.pose.pose.position 

    quaternion = (
        msg.pose.pose.orientation.x, 
        msg.pose.pose.orientation.y,
        msg.pose.pose.orientation.z,
        msg.pose.pose.orientation.w
    )
    rospy.loginfo(f"Quaternion = {quaternion}")

    euler = transformations.euler_from_quaternion(quaternion)
    rospy.loginfo(f"Euler = {euler}")
    time.sleep(2)
    yaw = euler[2]


def main():
    rospy.init_node("odometry_info")
    sub = rospy.Subscriber('/odom', Odometry, callback_odom) 
   
    rospy.spin()

if __name__ == '__main__':
    main()