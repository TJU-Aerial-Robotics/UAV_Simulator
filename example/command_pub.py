#!/usr/bin/env python3
import rospy
from _PositionCommand import PositionCommand
from geometry_msgs.msg import Point, Vector3

def publish_position_command():
    # 初始化ROS节点
    rospy.init_node('position_command_publisher', anonymous=True)
    
    # 创建Publisher
    pub = rospy.Publisher('/uav_0/so3_control/pos_cmd', PositionCommand, queue_size=10)
    
    # 设置发布频率
    rate = rospy.Rate(10)  # 10 Hz
    
    pos_x = 0.0

    while not rospy.is_shutdown():
        # 创建PositionCommand消息
        position_command = PositionCommand()
        
        # 填充消息内容
        position_command.header.stamp = rospy.Time.now()
        position_command.header.frame_id = "world"  # 假设在"world"坐标系下
        
        position_command.position = Point(pos_x, 0.0, 2.0)
        position_command.velocity = Vector3(0.0, 0.0, 0.0)
        position_command.acceleration = Vector3(0.0, 0.0, 0.0)
        
        position_command.yaw = 0.0  # 弧度，约90度
        
        position_command.trajectory_flag = 1  # 设置标志位
        
        # 发布消息
        pub.publish(position_command)

        pos_x = pos_x + 0.1
        # 休眠以保持发布频率
        rate.sleep()

if __name__ == "__main__":
    try:
        publish_position_command()
    except rospy.ROSInterruptException:
        pass
