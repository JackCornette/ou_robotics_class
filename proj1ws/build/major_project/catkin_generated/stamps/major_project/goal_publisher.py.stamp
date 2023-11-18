#!/usr/bin/env python

import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from std_msgs.msg import Int32MultiArray
from std_msgs.msg import String
from threading import Thread

class GoalPublisher:
	def __init__(self):
	    self.client = actionlib.SimpleActionClient('move_base', MoveBaseAction)
	    self.client.wait_for_server()
	    self.pause = False


	    # sends current goal marker to aruco_detector
	    self.custom_goal_pub = rospy.Publisher('custom_goal', Int32MultiArray, queue_size=10)
	    # aruco detector temporarily pauses goal sending when a aruco marker is found
	    self.aruco_detector_sub = rospy.Subscriber('aruco_detector', String, self.aruco_callback)
	
	    self.goals = [(3.0,-4.0, 1),(3.0, -1.0, 2),(-2.0, 5.0, 3),(0,0, 0)]
	    self.i = 0

            # Start a separate thread for sending goals
            self.goal_thread = Thread(target=self.send_goals_periodically)
            self.goal_thread.start()

	def send_goal(self, x, y, tag):

	    goal = MoveBaseGoal()
	    goal.target_pose.header.frame_id = "map"
	    goal.target_pose.pose.position.x = x
	    goal.target_pose.pose.position.y = y
	    goal.target_pose.pose.orientation.w = 1.0  # Facing forward

	    # tell aruco_detector what marker to look for
	    rospy.loginfo("SENDING GOAL: {}".format(tag))
	    self.custom_goal_pub.publish(Int32MultiArray(data=[x, y, tag]))
	    self.client.send_goal(goal)

	    self.client.wait_for_result()

        def send_goals_periodically(self):
            while not rospy.is_shutdown():

		while(self.pause): # don't send a new goal until marker detector has unpaused this node
		    pass

                self.send_goal(self.goals[self.i][0], self.goals[self.i][1], self.goals[self.i][2])  # unpause means tag reached so traverse to goal
                rospy.loginfo("Sent goal: ({}, {}) for tag={}".format(self.goals[self.i][0], self.goals[self.i][1], self.goals[self.i][2]))
                self.i += 1
                self.i = self.i % len(self.goals)
	    self.goal_thread.stop()

        def aruco_callback(self, data):
            if data.data == "pause":
		self.pause = True
                self.client.cancel_goal()  # pause means visual-homing is taking over
	    else:
		self.pause = False

if __name__ == '__main__':
    rospy.init_node('goal_publisher')
    goal_publisher = GoalPublisher()
    rospy.spin()
