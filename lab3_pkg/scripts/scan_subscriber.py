import numpy as np
import rospy
from sensor_msgs.msg import LaserScan

# ros Lidar RDS-01 data process

def callback(data):
    range_max = data.range_max
    range_min = data.range_min

    ranges_i = data.ranges
    ranges_i = np.array(ranges_i)
    ranges = ranges_i[ranges_i != 0]
    
    max = np.max(ranges)
    min = np.min(ranges)

    range_sort = []
    for i in ranges:
        i = round(i, 4)
        range_sort.append(i)
    range_sort = np.array(range_sort)
    range_sort.sort()

    rospy.loginfo("------------------------------ LaserScan ------------------------------")
    rospy.loginfo("Range_std: %.2f ~ %.2f m" % (range_min, range_max))

    rospy.loginfo("Ranges_sort: %s" % range_sort)
    rospy.loginfo("Range_max: %.2f m" % max)
    rospy.loginfo("Range_min: %.2f m" % min)    
    
if __name__ == '__main__':
    range_ref = 0.2
    rospy.init_node('scan_subscribe', anonymous=True)
    rospy.Subscriber('/scan', LaserScan, callback, queue_size=10)
    rospy.spin()
    
