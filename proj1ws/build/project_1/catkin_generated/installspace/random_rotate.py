#!/usr/bin/env python2
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist, Point
from nav_msgs.msg import Odometry
from tf.transformations import euler_from_quaternion
from random import uniform
import math


class RandomRotate(object):
    def __init__(self, speed=0.25, hz=10):
        
        self.pause = False
        self.max_distance = 1.0  # rotate every 1ft
        self.current_position = Point(0,0,0)
        self.start_position = self.current_position
        self.angular_velocity = speed
        self.rotate_degrees = 15 # rotate between -15 and +15
        self.rotating = False

        # Initialize the ROS node
        rospy.init_node('random_rotate')
        rospy.loginfo("random_rotate node started.")
        self.rate = rospy.Rate(hz)  # 10 Hz
        self.velocity_pub = rospy.Publisher('/mobile_base/commands/velocity', Twist, queue_size=10)

        # Create a subscriber for receiving messages from Topic A
        rospy.Subscriber('random_rotate', String, self.behavior_callback)
        rospy.Subscriber('/odom', Odometry, self.odom_callback)

        self.behavior_pub = rospy.Publisher('behavior', String, queue_size=10)


    # priority functionality
    def behavior_callback(self, data):
        rospy.loginfo("Random Rotate received %s message", data.data)
        
        if(data.data == "pause"):
            self.pause = True
            self.start_position = self.current_position
            self.rotating = False
        else:
            self.pause = False

    def odom_callback(self, msg):
        self.current_position = msg.pose.pose.position
        self.current_orientation = msg.pose.pose.orientation
        self.current_speed = msg.twist.twist.linear.x

    def calculate_distance(self, point1, point2):
        return math.sqrt((point1.x - point2.x) ** 2 + (point1.y - point2.y) ** 2)
    

    def run(self):
        while not rospy.is_shutdown():

            # drive is paused if a more important behavior is needed
            if(not self.pause):
                # Calculate the Euclidean distance between the current position and start position
                distance = self.calculate_distance(self.start_position, self.current_position)
                print(distance)
                # Randomly turn within +or- 15 degrees
                if distance >= self.max_distance:
                    print("randomly rotating")
                    
                    self.behavior_pub.publish("random_rotate")
                    
                    # Convert quaternion to Euler angles
                    (roll, pitch, current_yaw) = euler_from_quaternion(
                        [self.current_orientation.x, self.current_orientation.y, self.current_orientation.z, self.current_orientation.w])
                    print("currentYaw= ", current_yaw)
                    
                    if (not self.rotating):
                        self.rotating = True
                        # Calculate desired yaw after 15-degree rotation
                        angleDelta = uniform(-self.rotate_degrees, self.rotate_degrees)
                        desired_yaw = current_yaw + (angleDelta * 3.14159 / 180.0)
                        if(desired_yaw > math.pi):
                            desired_yaw = desired_yaw - 2*math.pi
                        elif(desired_yaw < -math.pi):
                            desired_yaw = desired_yaw + 2*math.pi
                        print("DesiredYaw= ", desired_yaw, "CurrentYaw= ", current_yaw)

                    # Create a Twist message to set the angular velocity for rotation
                    cmd_vel = Twist()
                    cmd_vel.linear.x = self.current_speed 
                    cmd_vel.angular.z = self.angular_velocity if angleDelta > 0 else -self.angular_velocity  # Adjust the angular velocity as needed

                    # Publish the Twist message
                    self.velocity_pub.publish(cmd_vel)

                    # Check if the desired orientation is reached
                    if abs(current_yaw - desired_yaw) < 0.075:
                        rospy.loginfo("Desired rotation angle reached.")
                        self.start_position = self.current_position
                        self.behavior_pub.publish("done_rotating")
                        cmd_vel = Twist()
                        cmd_vel.linear.x = self.current_speed
                        cmd_vel.angular.z = 0.0
                        self.velocity_pub.publish(cmd_vel)
                        self.rotating = False

            self.rate.sleep()


if __name__ == '__main__':
    try:
        behavior = RandomRotate()  # Initialize the class
        behavior.run()      # Start the behavior execution loop
    except rospy.ROSInterruptException:
        pass
