#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist
from kobuki_msgs.msg import BumperEvent

class Bumper(object):
    def __init__(self, speed=1.0, hz=10):
        
        self.pause = False
        self.twist = Twist()
        self.twist.linear.x = 0.0
        self.twist.angular.z = 0.0
        self.stop = False
        self.pressed_keys = set()

        # Initialize the ROS node
        rospy.init_node('bumper')
        rospy.loginfo("bumper node started.")
        self.rate = rospy.Rate(hz)
        self.velocity_pub = rospy.Publisher('/mobile_base/commands/velocity', Twist, queue_size=10)

        self.behavior_pub = rospy.Publisher('behavior', String, queue_size=10)

        self.bumper_subscriber = rospy.Subscriber('/mobile_base/events/bumper', BumperEvent, self.bumper_callback)        
        
    # if any bumper was pressed, stop
    def bumper_callback(self, data):
        if data.state == BumperEvent.PRESSED:
            rospy.loginfo("Collision detected")
            self.behavior_pub.publish("STOP")
            self.velocity_pub.publish(self.twist)

    def run(self):
        rospy.spin()



if __name__ == '__main__':
    try:
        behavior = Bumper()  # Initialize the class
        behavior.run()      # Start the behavior execution loop
    except rospy.ROSInterruptException:
        pass