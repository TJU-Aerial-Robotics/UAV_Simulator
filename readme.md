# UAV Simulator

**Acknowledgments:** This repo is modified from https://github.com/HKUST-Aerial-Robotics/Fast-Planner, thanks for their excellent work!

**USE:**
```bash
cd ${YOUR_WORKSPACE_PATH}/src
git clone https://github.com/TJU-Aerial-Robotics/UAV_Simulator
cd ../
catkin_make
source devel/setup.bash
roslaunch so3_quadrotor_simulator simulator.launch
```

**ROS Topics**

You can modify the topic names in the launch file.
The default simulated odometry topic is: `/sim/odom`, and the controller receives the topic: `/so3_control/pos_cmd`.

Where the odometry is standard ROS odometry message, and
you can send your control messages in the following format:

```cpp
#include "quadrotor_msgs/PositionCommand.h"
ros::Publisher pos_cmd_pub = node.advertise<quadrotor_msgs::PositionCommand>("/so3_cmd", 50);
quadrotor_msgs::PositionCommand cmd;
cmd.header.stamp = time_now;
cmd.header.frame_id = "world";

cmd.position.x = pos(0);
cmd.position.y = pos(1);
cmd.position.z = pos(2);

cmd.velocity.x = vel(0);
cmd.velocity.y = vel(1);
cmd.velocity.z = vel(2);

cmd.acceleration.x = acc(0);
cmd.acceleration.y = acc(1);
cmd.acceleration.z = acc(2);

cmd.yaw = yaw;
cmd.yaw_dot = yawdot;

pos_cmd_pub.publish(cmd);
```

**Updata:**
+ add the log recorder