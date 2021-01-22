#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32

def cb(message):
    rospy.loginfo(message.data)

if __name__ == '__main__':
    rospy.init_node('result')
    sub = rospy.Subscriber('calculator',Int32,cb)
    rospy.spin()
