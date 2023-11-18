#!/usr/bin/env python
import rospy
from sensor_msgs.msg import Image

def image_callback(data):
    # Extract the resolution from the incoming camera image message
    width = data.width
    height = data.height
    print("Camera resolution: {}x{}".format(width, height))

def main():
    rospy.init_node('camera_resolution_node')
    rospy.Subscriber('/camera/rgb/image_raw', Image, image_callback)  # Replace with your camera topic name
    rospy.spin()

if __name__ == '__main__':
    main()

