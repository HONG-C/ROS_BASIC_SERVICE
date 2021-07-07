#!/usr/bin/env python
# -*- coding: utf-8 -*-
#서버(정보를 요청할때 까지 기다리고 요청 오면 보내주고 종료)

from ros_basic_service.srv import*
import rospy

def handle_avoid_obstacle(req):
   print "Returning [%s + %s = %s]" %(req.a, req.b, (req.a+req.b))
   return AddTwoIntsResponse(req.a + req.b)

def avoid_obstacle():
   rospy.init_node('avoid_obstacle')
   s = rospy.Service('avoid_angle',AddTwoInts, handle_avoid_obstacle)
   print "Ready to get angle"
   rospy.spin()

if __name__=="__main__":
   avoid_obstacle()


