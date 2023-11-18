#!/usr/bin/env python2
# license removed for brevity
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist, Vector3

"""
drive_forward_behavior = DriveForward()
random_turn_behavior = RandomTurn()
avoid_behavior = Avoid()
escape_behavior = Escape()
keyboard_command = KeyboardCommand()
halt_behavior = Halt()
"""

class Behaviors():
    def __init__(self):
        
        self.drive_forward = True
        self.random_rotate = True
        self.avoid = True
        self.key_command = True


        # Initialize the ROS node
        rospy.init_node('behaviors')
        rospy.loginfo("behavior node started.")
        self.velocity_pub = rospy.Publisher('/mobile_base/commands/velocity', Twist, queue_size=10)

        # Create a subscriber for receiving messages from all other nodes
        rospy.Subscriber('behavior', String, self.behaviors_callback)

        # Create publishers to tell behaviors to stop/resume
        self.pub_drive_forward = rospy.Publisher('drive_forward', String, queue_size=10)
        self.pub_random_rotate = rospy.Publisher('random_rotate', String, queue_size=10)
        self.pub_avoid_escape = rospy.Publisher('avoid_escape', String, queue_size=10)
        self.pub_key_command = rospy.Publisher('key_command', String, queue_size=10)


    # higher priority behaviors essentially tell the lower level ones to pause
    def behaviors_callback(self, data):
        rospy.loginfo("Behavioral Message: %s", data.data)

        if(data.data == "STOP"):
            self.key_command = False
            self.avoid = False
            self.random_rotate = False

            self.pub_key_command.publish("pause")
            self.pub_avoid_escape.publish("pause")
            self.pub_random_rotate.publish("pause")
            self.pub_drive_forward.publish("pause")
        # if a key command is given and a higher priority isn't active
        elif(data.data == "key_command" and self.key_command):
            self.avoid = False
            self.random_rotate = False

            rospy.loginfo("key commands")
            self.pub_avoid_escape.publish("pause")
            self.pub_random_rotate.publish("pause")
            self.pub_drive_forward.publish("pause")

        elif(data.data == "no_command"):
            self.avoid = True
            self.random_rotate = True

            self.pub_avoid_escape.publish("resume")
            self.pub_random_rotate.publish("resume")
            self.pub_drive_forward.publish("resume")

        elif(data.data == "avoid" and self.avoid):
            self.random_rotate = False

            rospy.loginfo("avoiding")
            self.pub_random_rotate.publish("pause")
            self.pub_drive_forward.publish("pause")

        elif(data.data == "done_avoiding"):
            self.random_rotate = True
            self.pub_drive_forward.publish("resume")
            self.pub_random_rotate.publish("resume")    

        elif(data.data == "random_rotate" and self.random_rotate):
            self.pub_drive_forward.publish("pause")
            print("rotate")
        
        elif(data.data == "done_rotating"):
            self.pub_drive_forward.publish("resume")
            print("drive forward")


    def run(self):
        rospy.spin() # this node behaves as fast as the other behaviors reply to it


if __name__ == '__main__':
    try:
        behaviors = Behaviors()  # Initialize the Behaviors class
        behaviors.run()      # Start the behavior execution loop
    except rospy.ROSInterruptException:
        pass
