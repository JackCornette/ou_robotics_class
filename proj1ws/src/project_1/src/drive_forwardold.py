#!/usr/bin/env python

import rospy
import actionlib
# import DriveForwardAction, DriveForwardResult
from geometry_msgs.msg import Twist, Vector3

from action import DriveForwardAction, DriveForwardResult

# Define the DriveForwardAction server class
class DriveForwardServer(object):
    def __init__(self, name):
        
        self._action_name = name
        self._as = actionlib.SimpleActionServer(
            self._action_name,
            DriveForwardAction,
            execute_cb=self.execute_callback,
            auto_start=False
        )
        self._as.start()
        rospy.init_node('move_rotate', anonymous=True)
        rospy.loginfo("move_rotate node started.")
        hz = 10
        self.rate = rospy.Rate(hz)  # 10 Hz
        self.velocity_pub = rospy.Publisher('/mobile_base/commands/velocity', Twist, queue_size=10)
        self.speed = 1.0

    def execute_callback(self, goal):
        # Perform the "Drive Forward" behavior here
        # You can implement the behavior logic based on your requirements
        # For example, set the robot's linear velocity to drive forward
        # You can also use rospy.Rate() to control the behavior's execution rate

        while not rospy.is_shutdown():
            # Check if the action has been preempted (higher-priority behavior)
            if self._as.is_preempt_requested():
                rospy.loginfo("%s: Preempted" % self._action_name)

                self._as.set_preempted(DriveForwardResult())
                break

            velocity = Twist()
            # Implement "Drive Forward" behavior logic here
            # Set the robot's linear velocity or perform other actions
            # Drive forward until 1ft is reached
            velocity.linear = Vector3(self.speed,0,0) # Adjust linear velocity as needed
            self.velocity_pub.publish(velocity)
            # Publish control commands to control the robot's motion
            # For example, you can publish Twist messages to the /cmd_vel topic

            # Sleep to control the loop execution rate
            self.rate.sleep()

        # Action has finished (or preemption occurred)
        # Provide a result and finish the action
        result = DriveForwardResult()
        result.success = True
        self._as.set_succeeded(result)

if __name__ == '__main__':
    rospy.init_node('drive_forward_server')
    server = DriveForwardServer('drive_forward')
    rospy.spin()
