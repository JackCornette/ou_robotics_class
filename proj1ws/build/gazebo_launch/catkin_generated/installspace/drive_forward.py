#!/usr/bin/env python2
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist, Vector3


class DriveForward(object):
    def __init__(self, speed=0.75, hz=2):
        
        self.speed = speed
        self.pause = False

        # Initialize the ROS node
        rospy.init_node('drive_forward')
        rospy.loginfo("move_forawrd node started.")
        self.rate = rospy.Rate(hz)  # 10 Hz
        self.velocity_pub = rospy.Publisher('/mobile_base/commands/velocity', Twist, queue_size=10)

        # Create a subscriber for receiving messages from Topic A
        rospy.Subscriber('drive_forward', String, self.behavior_callback)


    # priority functionality
    def behavior_callback(self, data):
        rospy.loginfo("Forward Drive received %s message", data.data)
        
        if(data.data == "pause"):
            self.pause = True
        else:
            self.pause = False            


    def run(self):
        while not rospy.is_shutdown():

            # drive is paused if a more important behavior is needed
            if(not self.pause):
                velocity = Twist()
                # drive forward
                velocity.linear = Vector3(self.speed,0,0)
                self.velocity_pub.publish(velocity)

            self.rate.sleep()

if __name__ == '__main__':
    try:
        behavior = DriveForward()  # Initialize the class
        behavior.run()      # Start the behavior execution loop
    except rospy.ROSInterruptException:
        pass
