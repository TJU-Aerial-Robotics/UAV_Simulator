#!/usr/bin/env python3
import rospy
from visualization_msgs.msg import Marker
from geometry_msgs.msg import Point

def publish_lines():
    rospy.init_node('line_marker_publisher', anonymous=True)
    marker_pub = rospy.Publisher('boundary', Marker, queue_size=10)

    rate = rospy.Rate(1)  # 10 Hz

    while not rospy.is_shutdown():
        # 创建Marker对象
        marker = Marker()
        marker.header.frame_id = "world"  # 根据需要设置frame
        marker.header.stamp = rospy.Time.now()
        marker.ns = "lines"
        marker.id = 0
        marker.type = Marker.LINE_LIST  # 使用LINE_LIST类型
        marker.action = Marker.ADD

        # 设置线的颜色和尺寸
        marker.scale.x = 0.1  # 线的宽度
        marker.color.a = 1.0  # 不透明
        marker.color.r = 1.0
        marker.color.g = 0.0
        marker.color.b = 0.0

        # 添加线的点对 (每两个点定义一条直线)
        points = [
            Point(-10, -10, 0), Point(-10, 10, 0),  # 直线1的两个端点
            Point(-10, 10, 0), Point(10, 10, 0),  # 直线2的两个端点
            Point(10, 10, 0), Point(10, -10, 0),   # 直线3的两个端点
            Point(10, -10, 0), Point(-10, -10, 0)   # 直线3的两个端点
        ]
        marker.points.extend(points)

        # 发布Marker
        marker_pub.publish(marker)

        rate.sleep()

if __name__ == '__main__':
    try:
        publish_lines()
    except rospy.ROSInterruptException:
        pass
