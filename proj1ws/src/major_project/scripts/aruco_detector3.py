#!/usr/bin/env python

import rospy
from sensor_msgs.msg import Image, CameraInfo
from cv_bridge import CvBridge
import cv2
import cv2.aruco as aruco
import numpy as np
from geometry_msgs.msg import Twist
from std_msgs.msg import Int32MultiArray, String
from math import sqrt
import actionlib

from kobuki_msgs.msg import Sound, Led

"""
This node detects Aruco markers in the camera image. The goal_publisher node tells this node what tag to look for.
  When that tag is found in the camera, this node performs visual homing to drive towards the marker. Once the robot
  is close enough to the marker, it signals to the goal_publisher node to resume function and the process repeats.
"""

class ArUcoMarkerDetector:
    def __init__(self):
        self.bridge = CvBridge()
        self.image_sub = rospy.Subscriber('/camera/rgb/image_raw', Image, self.image_callback)
        self.cmd_vel_pub = rospy.Publisher('/mobile_base/commands/velocity', Twist, queue_size=1)

	# custom topics to handle behavior
        self.custom_goal_sub = rospy.Subscriber('custom_goal', Int32MultiArray, self.goal_callback)
	self.aruco_detector_pub = rospy.Publisher('aruco_detector', String, queue_size=10)

	# LED1 is map navigation, LED2 is visual homing navigation/ marker recognized. Sound played corresponds to marker found
	self.sound_pub = rospy.Publisher('mobile_base/commands/sound', Sound, queue_size=10)
        self.led1_pub = rospy.Publisher('mobile_base/commands/led1', Led, queue_size=10)
        self.led2_pub = rospy.Publisher('mobile_base/commands/led2', Led, queue_size=10)
	self.signal_autoNav()
	self.detected = False
	
	self.current_goal_coords = None
	self.current_goal_tag = 1
	self.thresh = 2.0

	# this stuff used to determine distance to aruco marker
	self.depth_sub = rospy.Subscriber('/camera/depth/image_raw', Image, self.depth_callback)
        self.camera_info_sub = rospy.Subscriber('/camera/depth/camera_info', CameraInfo, self.camera_info_callback)
	self.depth_image = None
        self.camera_info = None

    def depth_callback(self, data):
        self.depth_image = self.bridge.imgmsg_to_cv2(data, desired_encoding="passthrough")

    def camera_info_callback(self, data):
        self.camera_info = data

    def get_depth_at_marker_center(self, marker_center):
        # Get the depth information at the center of the ArUco marker
        u, v = marker_center
	u, v = int(u), int(v)
        depth_center = self.depth_image[v, u]
        
        # Convert depth to meters using camera information
        fx = self.camera_info.K[0]
        depth_center_meters = depth_center / fx

        return depth_center_meters

    # recieve the current tag to look for in camera
    def goal_callback(self, data):
	self.current_goal_coords = (data.data[0], data.data[1])
	self.current_goal_tag = data.data[2]
	rospy.loginfo("TAG: {}".format(self.current_goal_tag))

    def signal_homing(self):
	self.sound_pub.publish(Sound(1))
    	self.led1_pub.publish(Led(0))
       	self.led2_pub.publish(Led(1))

    def signal_autoNav(self):
	self.sound_pub.publish(Sound(4))
    	self.led1_pub.publish(Led(1))
       	self.led2_pub.publish(Led(0))

    def image_callback(self, data):
        cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")
        
        # ArUco marker detection
        gray = cv2.cvtColor(cv_image, cv2.COLOR_BGR2GRAY)
        aruco_dict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_4X4_50)
        parameters = cv2.aruco.DetectorParameters_create()
        corners, ids, rejectedImgPoints = cv2.aruco.detectMarkers(gray, aruco_dict, parameters=parameters)

	# extract marker we are currently looking for
        if ids is not None and corners is not None and self.current_goal_tag in ids:
	    for i, marker_id_detected in enumerate(ids):
                if marker_id_detected == self.current_goal_tag:
		    if not self.detected:
			self.signal_homing()
			self.detected = True

		    self.aruco_detector_pub.publish("pause")
		    rospy.loginfo("Marker seen")

		    target_marker_index = list(ids).index(self.current_goal_tag)
		    # Get the position of the detected target ArUco marker in camera view
		    marker_corners = corners[target_marker_index][0]
		    marker_center = np.mean(marker_corners, axis=0)
		    self.perform_homing_action(marker_center)

    def perform_homing_action(self, marker_center):
	marker_depth = self.get_depth_at_marker_center(marker_center)
	rospy.loginfo("Marker Depth: {}".format(marker_depth))
	if (marker_depth > self.thresh or marker_depth < 1.0):
	    
	    # Calculate error between the center of the image and the marker
	    error_x = marker_center[0] - 320  # Astra pro has 640x480 resolution
	    error_y = marker_center[1] - 240
	    if (abs(error_y) > 30 or abs(error_x) > 30): # prevent jitter
		    # Calculate angular velocity based on the error
		    self.angular_vel = -0.005 * error_x  # Adjust the gain for the angular velocity
		    # Calculate linear velocity based on the distance from the center
		    #distance = np.linalg.norm(marker_center - [320, 240])
		    #if(distance > 10):
		    #self.linear_vel = 0.01 * distance  # Adjust the gain for the linear velocity

		    rospy.loginfo("TWIST: {}, {}".format(0.5, self.angular_vel))

		    # Create Twist message to command the robot's motion
		    twist = Twist()
		    twist.linear.x = 0.5
		    twist.angular.z = self.angular_vel
		    self.cmd_vel_pub.publish(twist)
	    else:
		twist = Twist()
		twist.linear.x = 0.5
		twist.angular.z = self.angular_vel
		self.cmd_vel_pub.publish(twist)
	else:
	    self.signal_autoNav()
	    self.detected = False
	    rospy.loginfo("MARKER REACHED!!")
	    self.aruco_detector_pub.publish("resume")

def main():
    rospy.init_node('aruco_marker_detection_node')
    marker_detector = ArUcoMarkerDetector()
    rospy.spin()

if __name__ == '__main__':
    main()

