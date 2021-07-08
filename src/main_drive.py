#!/usr/bin/env python
# -*- coding: utf-8 -*-
#클라이언트(정보를 요청하는 부분)

import sys
import rospy
from ros_basic_service.srv import *

def main_drive(x,y):
   rospy.wait_for_service('avoid_angle')
   try:
      avoid_angle = rospy.ServiceProxy('avoid_angle', AvoidAngle)
      resp1 = avoid_angle(x,y)
      return resp1.sum
   except rospy.ServiceException, e:
      print "Service call failed: %s" %e

def usage():
   return "%s [x y]" %sys.argv[0]

if __name__=="__main__":
   if len(sys.argv) == 3 :
      x = int(sys.argv[1])
      y = int(sys.argv[2])
   else:
      print usage()
      sys.exit(1)

   print "Requesting %s + %s" %(x,y)
   print "%s + %s = %s" %(x, y, main_drive(x,y))


