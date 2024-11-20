A muti-uavs simulator, modified by Fast-Planner.

1. generate muti-uav launch file

```bash
python generate_launch.py
```

2. launch controller and simulator

```bash
catkin_make
source devel/setup.bash
roslaunch so3_quadrotor_simulator muti_simulator.launch
```

3. visualization

```bash
source devel/setup.bash
rviz -d src/swarm.rviz
```

4. pub the control command in you program
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

5. some Python example

5.1 pub control command 
```
python ./src/example/command_pub.py
```
5.2 pub Voronoi
```
python ./src/example/boundary_pub.py
```