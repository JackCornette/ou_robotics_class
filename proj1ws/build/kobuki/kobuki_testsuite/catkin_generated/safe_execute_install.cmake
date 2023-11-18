execute_process(COMMAND "/home/corn0038/ou_robotics_class/proj1ws/build/kobuki/kobuki_testsuite/catkin_generated/python_distutils_install.sh" RESULT_VARIABLE res)

if(NOT res EQUAL 0)
  message(FATAL_ERROR "execute_process(/home/corn0038/ou_robotics_class/proj1ws/build/kobuki/kobuki_testsuite/catkin_generated/python_distutils_install.sh) returned error code ")
endif()
