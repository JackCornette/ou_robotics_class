#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist, Vector3
from std_msgs.msg import Float32
from random import uniform
import math

def custom_robot_control():
    rospy.init_node('move_rotate', anonymous=True)
    rospy.loginfo("move_rotate node started.")
    hz = 10
    rate = rospy.Rate(hz)  # 10 Hz
    velocity_pub = rospy.Publisher('/mobile_base/commands/velocity', Twist, queue_size=10)

    distance = 0
    max_distance = 1.0  # 1ft = 0.3048 meters
    speed = 0.8
    angular_speed = 40

    # def left_encoder_callback(msg):
    #     global linear_distance, angular_distance
    #     # Assuming encoder data provides the number of wheel revolutions
    #     # and you know the wheel circumference and wheelbase
    #     wheel_revolutions = msg.data
    #     wheel_circumference = 0.2  # Example: wheel circumference in meters
    #     linear_distance += wheel_revolutions * wheel_circumference

    #     # Assuming the encoder data provides the number of wheel revolutions
    #     # and you know the wheelbase and wheel radius
    #     wheelbase = 0.3  # Example: wheelbase in meters
    #     wheel_radius = 0.05  # Example: wheel radius in meters
    #     wheel_travel = wheel_revolutions * wheel_radius
    #     angular_distance += wheel_travel / wheelbase

    while not rospy.is_shutdown():
        velocity = Twist()

        # Drive forward until 1ft is reached
        if distance < max_distance:
            velocity.linear = Vector3(speed,0,0) # Adjust linear velocity as needed
        else:
            velocity.linear = Vector3(0,0,0)

        # Randomly turn within +or- 15 degrees
        if distance >= max_distance:
            # get initial time 
            t_0 = rospy.Time.now().to_sec()
            angle = uniform(-15, 15)
            current_angle = 0

            uniform(-15, 15)  # 15 rads/sec range
            # convert angular speed to radian 
            angular_speed = math.radians(angular_speed)
            relative_angle = math.radians(angular_speed)
            velocity.angular.z = angular_speed
            # start rotating
            while current_angle < relative_angle:
                velocity_pub.publish(velocity)
                t_1 = rospy.Time.now().to_sec()
                current_angle = angular_speed*(t_1-t_0)

            # stop the rotation
            velocity.angular = Vector3(0,0,0)
            velocity_pub.publish(velocity)
            # for i in range(hz): # sleep for 1 second
            #     rate.sleep()
            # distance = 0 # restart driving
        else:
            distance += abs(velocity.linear.x / hz)  # Accumulate distance traveled

        velocity_pub.publish(velocity)
        rate.sleep()

if __name__ == '__main__':
    try:
        custom_robot_control()
    except rospy.ROSInterruptException:
        pass
