from pymycobot.mycobot import MyCobot
import pymycobot
from pymycobot import PI_PORT, PI_BAUD 
import time
import os
import sys
from pymycobot.genre import Angle
from pymycobot.mycobot import MyCobot
from pymycobot.genre import Coord
import time

mc = MyCobot("COM11", 115200)
mc.release_all_servos()


mc.set_gripper_value(100,50)
time.sleep(4)
mc.send_coords( [-235.8, 57.8, 251.8, -2.81, 40.81, -93.73],30)
time.sleep(2)
mc.send_coords( [-67.8, -25.3, 396.7, -81.4, 49.87, -135.8],30)
time.sleep(2)
mc.send_coords(  [-15.0, -79.5, 406.2, -87.98, 45.85, -136.27],30)
time.sleep(4)
mc.set_gripper_value(50,50)
time.sleep(2)
mc.send_coords(  [-124.9, -85.4, 322.2, -73.92, 40.16, -71.94],30)
time.sleep(2)
mc.send_coords( [55.0, -66.3, 341.2, -90.0, 45.0, -92.37],30)
time.sleep(4)
mc.set_gripper_value(100,50)
time.sleep(2)
mc.send_coords([-80.0, -80.8, 324.0, -70.41, 44.16, -73.6],30)
mc.sleep(2)
mc.set_gripper_value(100,20)







    
   
   
    
    