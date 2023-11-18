#!/usr/bin/env python

import rospy
import numpy as np
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2
import cv2.aruco as aruco
from geometry_msgs.msg import PointStamped, Point
from nav_msgs.msg import Odometry
from std_msgs.msg import Int32MultiArray
from std_msgs.msg import String
from tf import TransformListener
from math import sqrt
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal

"""
This node looks for aruco markers in the raw rgb camera data. The goal_publisher tells this node what marker
    to look for. When that marker is found in the camera, the pose of the marker is estimated, transformed to
    the map frame, and then those map coords are sent as a new goal for the turtlebot. When the turtlebot is
    close enough to the marker, it stops, plays an audio queue corresponding to the found marker, then signals
    to the goal_publisher that it can continue to a new aruco marker location.
"""

class ArucoGoal:
    def __init__(self):
        rospy.init_node('aruco_goal')

        self.camera_matrix = np.array([[627.4970741394926, 0, 319.8146775533469], [0, 627.7117564842846, 218.4486489713018], [0, 0, 1]], dtype=np.float64)
	self.camera_matrix = cv2.UMat(self.camera_matrix)
        self.distortion_coeffs = np.array([0.1792108601952825, -0.177727598703404, -0.01319396739234117, -0.005614194787872827, 0], dtype=np.float64)
	self.distortion_coeffs = cv2.UMat(self.distortion_coeffs)

        self.current_goal_coords = None

        self.bridge = CvBridge()
        self.listener = TransformListener()
        self.current_goal = None 
        self.marker_pose = None
        self.current_position = None
	self.moving_to_aruco = False
	self.current_goal_tag = 0

	# recieve camera data, aruco, and publish new goals
        rospy.Subscriber('/camera/rgb/image_raw', Image, self.image_callback)
	rospy.Subscriber('/odom', Odometry, self.odom_callback)
        self.goal_pub = rospy.Publisher('/move_base', MoveBaseAction, queue_size=10)

	# custom topics to handle behavior
        self.custom_goal_sub = rospy.Subscriber('custom_goal', Int32MultiArray, self.goal_callback)
	self.aruco_detector_pub = rospy.Publisher('aruco_detector', String, queue_size=10)

        self.dictionary = aruco.getPredefinedDictionary(aruco.DICT_4X4_50)
        self.marker_size = 0.2  # Size of the ArUco marker in meters
        self.marker_distance_threshold = 0.25  # Threshold distance to switch to ArUco marker as a goal
        self.detection_thresh = 0.1

    # monitor current position
    def odom_callback(self, data):
        self.current_position = data.pose.pose.position

    # recieve the current tag to look for in camera
    def goal_callback(self, data):
	self.current_goal_coords = (data.data[0], data.data[1])
	self.current_goal_tag = data.data[2]

    def image_callback(self, data):
	# convert raw data to cv usable image
        try:
            cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")
        except CvBridgeError as e:
            print(e)
            return

	# detect aruco markers in camera view
        gray = cv2.cvtColor(cv_image, cv2.COLOR_BGR2GRAY)
        parameters = aruco.DetectorParameters_create()
        corners, ids, _ = aruco.detectMarkers(gray, self.dictionary, parameters=parameters)

	# if markers are detected and one of them is the tag we are looking for, determine pose,
        #     send that as a new goal position and pause the goal_publisher
        if ids is not None and corners is not None and self.current_goal_tag in ids and not self.moving_to_aruco:
	    for i, marker_id_detected in enumerate(ids):
                if marker_id_detected == self.current_goal_tag:

		    # get aruco coords in map frame if coords are attainable from camera image
		    x, y = self.detect_coordinates(corners[i])
		    rospy.loginfo("aruco cords: ({}, {})".format(x,y))

		    # if the turtlebot is close enough to general area, send found aruco tag coords
		    #     aruco coord calc from far away is super innaccurate
		    distance = sqrt( 
                        (self.current_goal_coords[0] - x) ** 2 +
                        (self.current_goal_coords[1] - y) ** 2
                    )

		    if distance <= self.detection_thresh:
			    try: # Send coords to move_base so AMCL demo can navigate to it
				self.send_goal(x,y)
				rospy.loginfo("Found marker coords sent to map")
				
				self.aruco_detector_pub.publish("pause")
				self.moving_to_aruco = True
				self.marker_pose = Point()
				self.marker_pose.x = x
				self.marker_pose.y = y
			    except:
				rospy.loginfo("Failed to send aruco pose to map frame")
				pass

        if self.moving_to_aruco:
	    # determine distance between current_position and aruco marker
            distance = sqrt( 
                (self.current_position.x - self.marker_pose.x) ** 2 +
                (self.current_position.y - self.marker_pose.y) ** 2
            )
	    # if turtlebot is close enough to tag, stop and speak, then signal goal_publisher to continue
            if distance <= self.marker_distance_threshold:
		rospy.loginfo("Object reached!!") # Add sound here
		self.aruco_detector_pub.publish("resume") # Allows goal_publisher to send a new location/marker
		self.moving_to_aruco = False


    # determine coordinates of aruco marker in map frame
    def detect_coordinates(self, marker_corners):
        try:
            # Get aruco pose in camera frame
            rvec, tvec, _ = cv2.aruco.estimatePoseSingleMarkers(marker_corners, self.marker_size, self.camera_matrix, self.distortion_coeffs)
	    tvec = tvec.get()
            tvec = np.array([tvec[0][0][0], tvec[0][0][1], tvec[0][0][2]])

            # Get the current timestamp for transformation
            timestamp = rospy.Time(0)
            transformed_point = self.listener.transformPoint('/map', PointStamped(header=rospy.Header(stamp=timestamp, frame_id='/camera_link', seq=0), point=Point(x=tvec[0], y=tvec[1], z=tvec[2])))

            # return x,y map coords of aruco marker
            return transformed_point.point.x, transformed_point.point.y

        except Exception as e:
            rospy.logerr("Error: " + str(e))
		


    # Send new goal (location of aruco marker in map frame) to move_base (AMCL Demo uses move_base for nav)
    def send_goal(self, x, y):
        client = actionlib.SimpleActionClient('move_base', MoveBaseAction)
        client.wait_for_server()
        goal = MoveBaseGoal()
        goal.target_pose.header.frame_id = 'map'
        goal.target_pose.header.stamp = rospy.Time.now()
        goal.target_pose.pose.position.x = x
        goal.target_pose.pose.position.y = y
        goal.target_pose.pose.orientation.w = 1.0
      
        client.send_goal(goal)
        #self.client.wait_for_result()

def main():
    aruco_goal = ArucoGoal()
    rospy.spin()

if __name__ == '__main__':
    main()

