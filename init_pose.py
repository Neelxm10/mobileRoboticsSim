#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import PoseWithCovarianceStamped
from nav_msgs.msg import Odometry

# Node initialization
rospy.init_node('init_pose')
# pub = rospy.Publisher('/initialpose', PoseWithCovarianceStamped, queue_size = 1)
pub = rospy.Publisher('/odom', PoseWithCovarianceStamped, queue_size = 1)
# Construct message
init_msg = PoseWithCovarianceStamped()
init_msg.header.frame_id = "map"

# Get initial pose from Gazebo
# odom_msg = rospy.wait_for_message('/amcl_pose', Odometry)
# init_msg.pose.pose.position.x = odom_msg.pose.pose.position.x
# init_msg.pose.pose.position.y = odom_msg.pose.pose.position.y
# init_msg.pose.pose.orientation.x = odom_msg.pose.pose.orientation.x
# init_msg.pose.pose.orientation.y = odom_msg.pose.pose.orientation.y
# init_msg.pose.pose.orientation.z = odom_msg.pose.pose.orientation.z
# init_msg.pose.pose.orientation.w = odom_msg.pose.pose.orientation.w

init_msg.pose.pose.position.x = 0
init_msg.pose.pose.position.y = 0
init_msg.pose.pose.orientation.x = 0
init_msg.pose.pose.orientation.y = 0
init_msg.pose.pose.orientation.z = 0
init_msg.pose.pose.orientation.w = 1

# Delay
rospy.sleep(1)

# Publish message
rospy.loginfo("setting initial pose")
pub.publish(init_msg)
rospy.loginfo("initial pose is set")



# first run init_pose, then dont move the 2d pose estimate
# then teleop to the goal position, record that position in the goal_pose 
# script, then telop back to the init pose position and run goa_pose script
# fix local cost map inflation radius before running goal_pose
