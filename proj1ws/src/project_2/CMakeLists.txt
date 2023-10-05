cmake_minimum_required(VERSION 3.0.2)
project(project_1)

## Find catkin macros and libraries
## if COMPONENTS list like find_package(catkin REQUIRED COMPONENTS xyz)
## is used, also find other catkin packages
find_package(catkin REQUIRED COMPONENTS
  rospy
  std_msgs
  geometry_msgs
  sensor_msgs
  kobuki_msgs
  actionlib_msgs
  message_generation
)

###################################
## catkin specific configuration ##
###################################
## The catkin_package macro generates cmake config files for your package
## Declare things to be passed to dependent projects
## CATKIN_DEPENDS: catkin_packages dependent projects also need
catkin_package(
  CATKIN_DEPENDS rospy message_runtime std_msgs geometry_msgs sensor_msgs pynput kobuki_msgs
)

###########
## Build ##
###########

## Specify additional locations of header files
## Your package locations should be listed before other locations
include_directories(
# include
  ${catkin_INCLUDE_DIRS}
)



#############
## Install ##
#############

# all install targets should use catkin DESTINATION variables
# See http://ros.org/doc/api/catkin/html/adv_user_guide/variables.html

## Mark executable scripts (Python etc.) for installation
## in contrast to setup.py, you can choose the destination
catkin_install_python(
	PROGRAMS 
	src/behaviors.py 
	src/drive_forward.py 
	src/random_rotate.py 
	src/avoid_escape.py 
	src/key_command.py
	src/bumper.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)


