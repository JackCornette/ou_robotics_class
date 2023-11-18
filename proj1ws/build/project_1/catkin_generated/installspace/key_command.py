#!/usr/bin/env python2
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist
from pynput import keyboard
import threading

class KeyCommand(object):
    def __init__(self):
        
        self.pause = False
        self.twist = Twist()
        self.move = False
        self.turn = False

        # Initialize the ROS node
        rospy.init_node('key_command')
        rospy.loginfo("key_command node started.")
        self.velocity_pub = rospy.Publisher('/mobile_base/commands/velocity', Twist, queue_size=10)

        # unique set of all keys currently being pressed
        self.pressed_keys = set()

        # Create pubs and subs for keyboard and behavior 
        rospy.Subscriber('key_command', String, self.behavior_callback)

        self.behavior_pub = rospy.Publisher('behavior', String, queue_size=10)
        # This library creates a new thread
        self.listener = keyboard.Listener(on_release=self.on_key_release, on_press=self.on_key_press)
        self.listener.start()


    # process commands from behvaior node
    def behavior_callback(self, data):
        rospy.loginfo("Key Command received %s message", data.data)
        
        if(data.data == "pause"):
            self.pause = True
        else:
            self.pause = False

    def on_key_press(self, key):
        try:
            print("pressed: ", key.char)
            self.pressed_keys.add(key)
            print(self.pressed_keys)

            if not self.pause:
                if key.char == 'w':
                    self.twist.linear.x = 0.35  # Forward motion
                    self.move = True
                elif key.char == 's':
                    self.twist.linear.x = -0.25  # Backward motion
                    self.move = True
                if key.char == 'a':
                    self.twist.angular.z = 0.75  # Turn left
                    self.turn = True
                elif key.char == 'd':
                    self.twist.angular.z = -0.75  # Turn right
                    self.turn = True
                
                if(self.move or self.turn):
                        self.behavior_pub.publish("key_command")
                        self.velocity_pub.publish(self.twist)
            
        except AttributeError:
            # Key is not a character key or not recognized
            pass

    def on_key_release(self, key):
        try:
            print("released: ", key.char)
            self.pressed_keys.remove(key)

            if not self.pause:
                if key.char == 'w':
                    self.twist.linear.x = 0.0  # Forward motion
                elif key.char == 's':
                    self.twist.linear.x = 0.0  # Backward motion
                if key.char == 'a':
                    self.twist.angular.z = 0.0  # Turn left
                elif key.char == 'd':
                    self.twist.angular.z = 0.0  # Turn right

                self.velocity_pub.publish(self.twist)

                if len(self.pressed_keys) == 0:
                    print("no keys")
                    self.behavior_pub.publish("no_command")

        except AttributeError:
            # Key is not a character key or not recognized or key was not in pressed_keys
            pass

    def run(self):
        rospy.spin() # this node responds as fast as the keyboard input can be read



if __name__ == '__main__':
    try:
        behavior = KeyCommand()  # Initialize the Behaviors class
        behavior.run()      # Start the behavior execution loop
    except rospy.ROSInterruptException:
        pass
