# UAV Simulator

This repo is modified from https://github.com/HKUST-Aerial-Robotics/Fast-Planner

**Use:**
```bash
cd ${YOUR_WORKSPACE_PATH}/src
git clone https://github.com/Lu-tju/UAV_Simulator
cd ../
catkin_make
source devel/setup.bash
roslaunch so3_quadrotor_simulator simulator.launch
```

**ROS Topics**
You can modify the topic names in the launch file.
The default simulated odometry topic is: `/sim/odom`, and the controller receives the topic: `/so3_control/pos_cmd`.

Where the odometry is a standard ROS odometry message.
You can send control messages in the following format:

**updata:**
+ add the log recorder