# Project Workspace

This workspace contains the necessary directories for building and running a ROS (Robot Operating System) project. It includes the following main folders:

- `src`: This directory is where the ROS packages and source code are. It contains different project's custom nodes, launch files, and other code.

- `devel`: The `devel` directory is generated when you build your ROS workspace using tools like `catkin_make`. It contains the compiled binaries and libraries generated from your source code. These compiled files are used for running your ROS nodes and packages.

- `build`: The `build` directory is also generated during the build process. It contains intermediate build files and is used in the compilation process. You generally don't need to interact with this directory directly.

## Setting Up the Workspace

Install ROS melodic using `sudo apt-get install ros-melodic-desktop-full`

When first cloning this repository, use catkin_make to initialize the workspace.

At the beginning of a session in a new terminal, naviagte to this directiory and use `source devel/setup.bash`

This is considred the catkin workspace, and any changes made must be rebuilt using `catkin_make`.
