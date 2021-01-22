#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32

if __name__ == "__main__":
    rospy.init_node('input')
    pub = rospy.Publisher('calculator',Int32,queue_size=1)
    while not rospy.is_shutdown():
        print('演算子を選んでください')
        print('+:1, -:2, *:3, /:4')
        op = int(input())
        if op == 1:
            print('+')
            a = int(input())
            b = int(input())
            c = a + b
            print('%d + %d ' %(a,b))
            pub.publish(c)

        elif op == 2:
            print('-')
            a = int(input())
            b = int(input())
            c = a - b
            print('%d - %d ' %(a,b))
            pub.publish(c)

        elif op == 3:
            print('*')
            a = int(input())
            b = int(input())
            c = a * b
            print('%d * %d ' %(a,b))
            pub.publish(c)
           
        elif op == 4:
              print('/')
              a = int(input())
              b = int(input())
              c = a // b
              print('%d / %d ' %(a,b))
              pub.publish(c)

        else:
            print("error")


            
