# Install script for directory: /home/corn0038/ou_robotics_class/proj1ws/src

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/home/corn0038/ou_robotics_class/proj1ws/install")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "FALSE")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  
      if (NOT EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}")
        file(MAKE_DIRECTORY "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}")
      endif()
      if (NOT EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/.catkin")
        file(WRITE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/.catkin" "")
      endif()
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
   "/home/corn0038/ou_robotics_class/proj1ws/install/_setup_util.py")
  if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
file(INSTALL DESTINATION "/home/corn0038/ou_robotics_class/proj1ws/install" TYPE PROGRAM FILES "/home/corn0038/ou_robotics_class/proj1ws/build/catkin_generated/installspace/_setup_util.py")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
   "/home/corn0038/ou_robotics_class/proj1ws/install/env.sh")
  if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
file(INSTALL DESTINATION "/home/corn0038/ou_robotics_class/proj1ws/install" TYPE PROGRAM FILES "/home/corn0038/ou_robotics_class/proj1ws/build/catkin_generated/installspace/env.sh")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
   "/home/corn0038/ou_robotics_class/proj1ws/install/setup.bash;/home/corn0038/ou_robotics_class/proj1ws/install/local_setup.bash")
  if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
file(INSTALL DESTINATION "/home/corn0038/ou_robotics_class/proj1ws/install" TYPE FILE FILES
    "/home/corn0038/ou_robotics_class/proj1ws/build/catkin_generated/installspace/setup.bash"
    "/home/corn0038/ou_robotics_class/proj1ws/build/catkin_generated/installspace/local_setup.bash"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
   "/home/corn0038/ou_robotics_class/proj1ws/install/setup.sh;/home/corn0038/ou_robotics_class/proj1ws/install/local_setup.sh")
  if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
file(INSTALL DESTINATION "/home/corn0038/ou_robotics_class/proj1ws/install" TYPE FILE FILES
    "/home/corn0038/ou_robotics_class/proj1ws/build/catkin_generated/installspace/setup.sh"
    "/home/corn0038/ou_robotics_class/proj1ws/build/catkin_generated/installspace/local_setup.sh"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
   "/home/corn0038/ou_robotics_class/proj1ws/install/setup.zsh;/home/corn0038/ou_robotics_class/proj1ws/install/local_setup.zsh")
  if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
file(INSTALL DESTINATION "/home/corn0038/ou_robotics_class/proj1ws/install" TYPE FILE FILES
    "/home/corn0038/ou_robotics_class/proj1ws/build/catkin_generated/installspace/setup.zsh"
    "/home/corn0038/ou_robotics_class/proj1ws/build/catkin_generated/installspace/local_setup.zsh"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
   "/home/corn0038/ou_robotics_class/proj1ws/install/.rosinstall")
  if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
file(INSTALL DESTINATION "/home/corn0038/ou_robotics_class/proj1ws/install" TYPE FILE FILES "/home/corn0038/ou_robotics_class/proj1ws/build/catkin_generated/installspace/.rosinstall")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for each subdirectory.
  include("/home/corn0038/ou_robotics_class/proj1ws/build/gtest/cmake_install.cmake")
  include("/home/corn0038/ou_robotics_class/proj1ws/build/ros_astra_launch/cmake_install.cmake")
  include("/home/corn0038/ou_robotics_class/proj1ws/build/kobuki/kobuki/cmake_install.cmake")
  include("/home/corn0038/ou_robotics_class/proj1ws/build/kobuki/kobuki_capabilities/cmake_install.cmake")
  include("/home/corn0038/ou_robotics_class/proj1ws/build/kobuki_desktop/kobuki_desktop/cmake_install.cmake")
  include("/home/corn0038/ou_robotics_class/proj1ws/build/kobuki_desktop/kobuki_gazebo/cmake_install.cmake")
  include("/home/corn0038/ou_robotics_class/proj1ws/build/kobuki/kobuki_rapps/cmake_install.cmake")
  include("/home/corn0038/ou_robotics_class/proj1ws/build/kobuki_desktop/kobuki_rviz_launchers/cmake_install.cmake")
  include("/home/corn0038/ou_robotics_class/proj1ws/build/kobuki_msgs/cmake_install.cmake")
  include("/home/corn0038/ou_robotics_class/proj1ws/build/turtlebot/turtlebot/cmake_install.cmake")
  include("/home/corn0038/ou_robotics_class/proj1ws/build/turtlebot_apps/turtlebot_apps/cmake_install.cmake")
  include("/home/corn0038/ou_robotics_class/proj1ws/build/turtlebot/turtlebot_bringup/cmake_install.cmake")
  include("/home/corn0038/ou_robotics_class/proj1ws/build/turtlebot/turtlebot_capabilities/cmake_install.cmake")
  include("/home/corn0038/ou_robotics_class/proj1ws/build/turtlebot_interactions/turtlebot_dashboard/cmake_install.cmake")
  include("/home/corn0038/ou_robotics_class/proj1ws/build/turtlebot_simulator/turtlebot_gazebo/cmake_install.cmake")
  include("/home/corn0038/ou_robotics_class/proj1ws/build/turtlebot_interactions/turtlebot_interactions/cmake_install.cmake")
  include("/home/corn0038/ou_robotics_class/proj1ws/build/turtlebot_apps/turtlebot_rapps/cmake_install.cmake")
  include("/home/corn0038/ou_robotics_class/proj1ws/build/turtlebot_interactions/turtlebot_rviz_launchers/cmake_install.cmake")
  include("/home/corn0038/ou_robotics_class/proj1ws/build/turtlebot_simulator/turtlebot_simulator/cmake_install.cmake")
  include("/home/corn0038/ou_robotics_class/proj1ws/build/turtlebot_simulator/turtlebot_stage/cmake_install.cmake")
  include("/home/corn0038/ou_robotics_class/proj1ws/build/turtlebot_simulator/turtlebot_stdr/cmake_install.cmake")
  include("/home/corn0038/ou_robotics_class/proj1ws/build/kobuki_keyop/cmake_install.cmake")
  include("/home/corn0038/ou_robotics_class/proj1ws/build/openni2_camera/openni2_launch/cmake_install.cmake")
  include("/home/corn0038/ou_robotics_class/proj1ws/build/kobuki/kobuki_auto_docking/cmake_install.cmake")
  include("/home/corn0038/ou_robotics_class/proj1ws/build/ros_astra_camera/cmake_install.cmake")
  include("/home/corn0038/ou_robotics_class/proj1ws/build/depthimage_to_laserscan/cmake_install.cmake")
  include("/home/corn0038/ou_robotics_class/proj1ws/build/kobuki_bumper2pc/cmake_install.cmake")
  include("/home/corn0038/ou_robotics_class/proj1ws/build/major_project/cmake_install.cmake")
  include("/home/corn0038/ou_robotics_class/proj1ws/build/openni2_camera/openni2_camera/cmake_install.cmake")
  include("/home/corn0038/ou_robotics_class/proj1ws/build/project_1/cmake_install.cmake")
  include("/home/corn0038/ou_robotics_class/proj1ws/build/rgbd_launch/cmake_install.cmake")
  include("/home/corn0038/ou_robotics_class/proj1ws/build/kobuki_desktop/kobuki_dashboard/cmake_install.cmake")
  include("/home/corn0038/ou_robotics_class/proj1ws/build/robot_pose_ekf/cmake_install.cmake")
  include("/home/corn0038/ou_robotics_class/proj1ws/build/turtlebot_apps/turtlebot_actions/cmake_install.cmake")
  include("/home/corn0038/ou_robotics_class/proj1ws/build/turtlebot_apps/turtlebot_calibration/cmake_install.cmake")
  include("/home/corn0038/ou_robotics_class/proj1ws/build/turtlebot_interactions/turtlebot_interactive_markers/cmake_install.cmake")
  include("/home/corn0038/ou_robotics_class/proj1ws/build/turtlebot_msgs/cmake_install.cmake")
  include("/home/corn0038/ou_robotics_class/proj1ws/build/turtlebot_apps/turtlebot_follower/cmake_install.cmake")
  include("/home/corn0038/ou_robotics_class/proj1ws/build/turtlebot_apps/turtlebot_navigation/cmake_install.cmake")
  include("/home/corn0038/ou_robotics_class/proj1ws/build/turtlebot/turtlebot_teleop/cmake_install.cmake")
  include("/home/corn0038/ou_robotics_class/proj1ws/build/kobuki_desktop/kobuki_gazebo_plugins/cmake_install.cmake")
  include("/home/corn0038/ou_robotics_class/proj1ws/build/kobuki_description/cmake_install.cmake")
  include("/home/corn0038/ou_robotics_class/proj1ws/build/turtlebot/turtlebot_description/cmake_install.cmake")
  include("/home/corn0038/ou_robotics_class/proj1ws/build/yocs_cmd_vel_mux/cmake_install.cmake")
  include("/home/corn0038/ou_robotics_class/proj1ws/build/yocs_controllers/cmake_install.cmake")
  include("/home/corn0038/ou_robotics_class/proj1ws/build/kobuki/kobuki_controller_tutorial/cmake_install.cmake")
  include("/home/corn0038/ou_robotics_class/proj1ws/build/kobuki/kobuki_random_walker/cmake_install.cmake")
  include("/home/corn0038/ou_robotics_class/proj1ws/build/kobuki_safety_controller/cmake_install.cmake")
  include("/home/corn0038/ou_robotics_class/proj1ws/build/kobuki_node/cmake_install.cmake")
  include("/home/corn0038/ou_robotics_class/proj1ws/build/kobuki/kobuki_testsuite/cmake_install.cmake")

endif()

if(CMAKE_INSTALL_COMPONENT)
  set(CMAKE_INSTALL_MANIFEST "install_manifest_${CMAKE_INSTALL_COMPONENT}.txt")
else()
  set(CMAKE_INSTALL_MANIFEST "install_manifest.txt")
endif()

string(REPLACE ";" "\n" CMAKE_INSTALL_MANIFEST_CONTENT
       "${CMAKE_INSTALL_MANIFEST_FILES}")
file(WRITE "/home/corn0038/ou_robotics_class/proj1ws/build/${CMAKE_INSTALL_MANIFEST}"
     "${CMAKE_INSTALL_MANIFEST_CONTENT}")