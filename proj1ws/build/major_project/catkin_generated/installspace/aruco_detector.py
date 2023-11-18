#!/usr/bin/env python2

import rospy
from cv2 import aruco
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
from geometry_msgs.msg import PoseWithCovarianceStamped
from std_msgs.msg import String

class ArUcoMarkerDetector:
    def __init__(self):
        rospy.init_node('aruco_marker_detector')

        self.bridge = CvBridge()

        self.image_sub = rospy.Subscriber('/camera/rgb/image_raw', Image, self.image_callback)
        self.initial_pose_pub = rospy.Publisher('/initialpose', PoseWithCovarianceStamped, queue_size=1)
        self.custom_goal_pub = rospy.Publisher('/custom_goal', String, queue_size=1)

        self.aruco_dict = aruco.Dictionary_get(aruco.DICT_4X4_50)
        self.parameters = aruco.DetectorParameters_create()

        self.goal_markers = {
            1: 'goal1',  # Adjust marker IDs and goal names accordingly
            2: 'goal2',
            3: 'goal3'
        }

    def image_callback(self, data):
        try:
            cv_image = self.bridge.imgmsg_to_cv2(data, 'bgr8')
        except CvBridgeError as e:
            rospy.logerr(e)
            return

        # Detect ArUco markers
        corners, ids, _ = aruco.detectMarkers(cv_image, self.aruco_dict, parameters=self.parameters)

        if ids is not None:
	    print("Marker found: ", ids[0][0])
#            for marker_id in ids:
#                if marker_id in self.goal_markers:
#                    goal_name = self.goal_markers[marker_id]
#                    self.send_custom_goal(goal_name)

    def send_custom_goal(self, goal_name):
        rospy.loginfo("ArUco marker detected: {}".format(goal_name))
        custom_goal = String()
        custom_goal.data = goal_name
        self.custom_goal_pub.publish(custom_goal)

if __name__ == '__main__':
    try:
        detector = ArUcoMarkerDetector()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass

