#!/usr/bin/env python2
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan
from nav_msgs.msg import Odometry
from tf.transformations import euler_from_quaternion
import math
from random import uniform

class AvoidEscape(object):
    def __init__(self, speed=0.25, hz=10):
        
        self.pause = False
        self.rotating = False
        self.min_distance_threshold = 1.0  # Minimum distance to trigger obstacle avoidance
        self.angular_velocity = 0.5  # Angular velocity for turning

        self.turning_around = False
        self.left_obstacle_detected = False
        self.right_obstacle_detected = False
        self.symmetric = 0.1

        self.current_orientation = 0
        self.current_speed = 0


        # Initialize the ROS node
        rospy.init_node('avoid_escape')
        rospy.loginfo("avoid_escape node started.")
        self.rate = rospy.Rate(hz)  # 10 Hz
        self.velocity_pub = rospy.Publisher('/mobile_base/commands/velocity', Twist, queue_size=10)

        # Create a subscriber for receiving messages from Topic A
        rospy.Subscriber('avoid_escape', String, self.behavior_callback)
        # subscribe to the LiDar sensor 
        rospy.Subscriber('/scan', LaserScan, self.laser_callback)
        # subscribe to the LiDar sensor
        rospy.Subscriber('/odom', Odometry, self.odom_callback)
        self.behavior_pub = rospy.Publisher('behavior', String, queue_size=10)


    # priority functionality
    def behavior_callback(self, data):
        rospy.loginfo("Avoid_escape received %s message", data.data)
        
        if(data.data == "pause"):
            self.pause = True
            self.rotating = False
            self.turning_around = False
        else:
            self.pause = False

    def odom_callback(self, msg):
        self.current_orientation = msg.pose.pose.orientation

    def calc_min_distances(self, msg):
        # msg.ranges contains the Laser Scan array
        midpoint = int((len(msg.ranges)) / 2)

        right_min = min(msg.ranges[0:midpoint])
        left_min = min(msg.ranges[midpoint:])

        if(math.isnan(right_min)):
            right_min = 9999
        if(math.isnan(left_min)):
            left_min = 9999

        return right_min, left_min 

    # The rate the LaserScan publishes at is essentially how fast this behavior responds
    def laser_callback(self, msg):

        # find the closest point on both sides to determine symmetry
        self.min_left_distance, self.min_right_distance = self.calc_min_distances(msg)

        rospy.loginfo("Minimum Distances: L({0}) R({1})".format(self.min_left_distance, self.min_right_distance))

        if not self.pause:
            if self.turning_around:
                self.turn_180_degrees()
            # object detected on both sides
            elif self.min_left_distance < self.min_distance_threshold and self.min_right_distance < self.min_distance_threshold:
                if abs(self.min_left_distance - self.min_right_distance) < self.symmetric:
                    # Roughly symmetric obstacle on both sides, turn 180 degrees
                    # Calculate desired yaw after 180-degree rotation
                    (roll, pitch, current_yaw) = euler_from_quaternion(
                    [self.current_orientation.x, self.current_orientation.y, self.current_orientation.z, self.current_orientation.w])
                    if(current_yaw > 0):
                        self.desired_yaw = current_yaw - math.pi
                    else:
                        self.desired_yaw = current_yaw + math.pi
                    print("Currentyaw: ", current_yaw, "desiredyaw: ", self.desired_yaw)

                    self.behavior_pub.publish("avoid")
                    rospy.loginfo("turn around")
                    self.turn_180_degrees()
                elif self.min_right_distance > self.min_left_distance:
                    # Obstacle detected on the left and right, but object on left is closer, turn right to avoid it
                    self.behavior_pub.publish("avoid")
                    rospy.loginfo("avoid_right")
                    self.rotating = True
                    self.turn_right()
                else:
                    # Obstacle detected on the left and right, but object on right is closer, turn left to avoid it
                    self.behavior_pub.publish("avoid")
                    rospy.loginfo("avoid_left")
                    self.rotating = True
                    self.turn_left()
            elif self.min_right_distance < self.min_distance_threshold:
                # Obstacle detected on the right and nothing on left so turn
                self.behavior_pub.publish("avoid")
                rospy.loginfo("avoid_left")
                self.rotating = True
                self.turn_left()
            elif self.min_left_distance < self.min_distance_threshold:
                # Obstacle detected on the left, start turning right to avoid it
                self.behavior_pub.publish("avoid")
                rospy.loginfo("avoid_right")
                self.rotating = True
                self.turn_right()
            elif self.rotating and self.min_left_distance > self.min_distance_threshold and self.min_right_distance > self.min_distance_threshold:
                # Obstacles detected are now out of sight so stop turning and allow other behaviors to continue
                self.stop_turning()
                self.rotating = False
                rospy.loginfo("stopped turning")
                self.behavior_pub.publish("done_avoiding")
            else:
                self.behavior_pub.publish("no objects detected")
                rospy.loginfo("No object detected")


    def turn_right(self):
        twist = Twist()
        twist.linear.x = 0.0
        twist.angular.z = self.angular_velocity  # Rotate right to avoid the obstacle
        self.velocity_pub.publish(twist)

    def turn_left(self):
        twist = Twist()
        twist.linear.x = 0.0
        twist.angular.z = -self.angular_velocity  # Rotate left to avoid the obstacle
        self.velocity_pub.publish(twist)

    def stop_turning(self):
        twist = Twist()
        twist.linear.x = 0.0
        twist.angular.z = 0.0  # Stop turning
        self.velocity_pub.publish(twist)

    def turn_180_degrees(self):
        self.turning_around = True
        # Convert quaternion to Euler angles
        (roll, pitch, current_yaw) = euler_from_quaternion(
            [self.current_orientation.x, self.current_orientation.y, self.current_orientation.z, self.current_orientation.w])
        print(current_yaw)
        # Create a Twist message to set the angular velocity for rotation
        twist = Twist()
        twist.linear.x = 0.0
        twist.angular.z = self.angular_velocity

        # Publish the Twist message
        self.velocity_pub.publish(twist)

        # Check if the desired orientation is reached
        if abs(current_yaw - self.desired_yaw) < uniform(0, 0.523599): # + or - 30 degrees (in radians) of target
            rospy.loginfo("Desired 180 rotation reached.")
            self.behavior_pub.publish("done_avoiding")
            twist = Twist()
            twist.angular.z = 0.0
            self.velocity_pub.publish(twist)
            self.turning_around = False

    def run(self): # allows the node to recieve subscribed messages
        rospy.spin()


if __name__ == '__main__':
    try:
        behavior = AvoidEscape()  # Initialize the class
        behavior.run()
    except rospy.ROSInterruptException:
        pass
