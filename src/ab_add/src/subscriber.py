#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32

num1 = None
num2 = None

def callback1(msg):
    global num1
    num1 = msg.data
    calculate_sum()

def callback2(msg):
    global num2
    num2 = msg.data
    calculate_sum()

def calculate_sum():
    if num1 is not None and num2 is not None:
        print(f"和是: {num1 + num2}")

def subscriber():
    rospy.init_node('sum_subscriber', anonymous=True)
    rospy.Subscriber('number1', Int32, callback1)
    rospy.Subscriber('number2', Int32, callback2)
    rospy.spin()

if __name__ == '__main__':
    subscriber()
