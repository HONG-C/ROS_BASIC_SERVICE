#!/usr/bin/env python
# -*- coding: utf-8 -*-
#서버(정보를 요청할때 까지 기다리고 요청 오면 보내주고 종료)

from ros_basic_service.srv import*
import rospy

def handle_add_two_ints(req):
   print "Returning [%s + %s = %s]" %(req.a, req.b, (req.a+req.b))
   return AddTwoIntsResponse(req.a + req.b)

def add_two_ints_server():
   rospy.init_node('avoid_obstacle')
   s = rospy.Service('add_two_ints',avoid_angle, handle_add_two_ints)
   print "Ready to add two ints."
   rospy.spin()

if __name__=="__main__":
   add_two_ints_server()


