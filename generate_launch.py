# 修改无人机的数量以及位置等信息，python generate_launch.py生成launch文件
import os
import random

N_uav = 3

launch_content = '<launch>\n'

for i in range(N_uav):
    random_x = random.randint(0, 10)
    random_y = random.randint(0, 10)
    random_z = 2
    random_team = random.randint(0, 1)
    node_name = f'uav_{i}'
    launch_content += f"""
  <group ns="{node_name}">
    <node pkg="so3_quadrotor_simulator" type="quadrotor_simulator_so3" name="simulator" output="screen">
      <param name="rate/odom" value="50.0"/>
      <param name="team" value="{random_team}"/>
      <param name="simulator/init_state_x" value="{random_x}"/>
      <param name="simulator/init_state_y" value="{random_y}"/>
      <param name="simulator/init_state_z" value="{random_z}"/>
      <remap from="~odom_juliett" to="/{node_name}/sim/odom_juliett"/>
      <remap from="~odom" to="/{node_name}/sim/odom"/>
      <remap from="~imu" to="/{node_name}/sim/imu"/>
      <remap from="~cmd" to="/{node_name}/so3_cmd"/>   
    </node>

    <node pkg="nodelet" type="nodelet" args="standalone so3_control/SO3ControlNodelet" name="controller" required="true" output="screen">
        <param name="so3_control/init_state_x" value="{random_x}"/>
        <param name="so3_control/init_state_y" value="{random_y}"/>
        <param name="so3_control/init_state_z" value="{random_z}"/>
        <remap from="~odom" to="/{node_name}/sim/odom"/>
        <remap from="~imu" to="/{node_name}/sim/imu"/>
        <remap from="~position_cmd" to="/{node_name}/so3_control/pos_cmd"/>
        <remap from="~so3_cmd" to="/{node_name}/so3_cmd"/>
        <rosparam file="$(find so3_control)/config/gains_hummingbird.yaml"/>
        <rosparam file="$(find so3_control)/config/corrections_hummingbird.yaml"/>
        <param name="mass" value="0.98"/>
        <param name="use_angle_corrections " value="false"/>
        <param name="use_external_yaw "      value="false"/>
        <param name="gains/rot/z" value="1.0"/>    
        <param name="gains/ang/z" value="0.1"/>     
        <param name="record_log" value = "false"/>  
        <param name="PID_logger_file_name" value = "$(find so3_control)/logger/"/>   
    </node>
  </group>  
  """

launch_content += '</launch>'

# 将内容写入文件
with open(os.path.join(os.path.dirname(__file__), 'so3_quadrotor_simulator/launch', 'muti_simulator.launch'), 'w') as f:
    f.write(launch_content)

print("Launch file generated: so3_quadrotor_simulator/launch/muti_simulator.launch")
