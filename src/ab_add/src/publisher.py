#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32

def publisher():
    rospy.init_node('number_publisher', anonymous=True)
    pub1 = rospy.Publisher('number1', Int32, queue_size=10)
    pub2 = rospy.Publisher('number2', Int32, queue_size=10)
    rate = rospy.Rate(1)  # 1 Hz
    while not rospy.is_shutdown():
        try:
            num1 = int(input("请输入第一个数字: "))
            num2 = int(input("请输入第二个数字: "))
        except ValueError:
            print("请输入整数！")
            continue
        pub1.publish(num1)
        pub2.publish(num2)
        print(f"已发布: {num1}, {num2}")
        rate.sleep()

if __name__ == '__main__':
    try:
        publisher()
    except rospy.ROSInterruptException:
        pass
