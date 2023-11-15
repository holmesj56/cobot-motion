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


mc = MyCobot("COM9", 115200)
mc.send_angles([0,90,-45,0,0,0],30)
time.sleep(2)
mc.release_all_servos()
mc.send_angles([0,90,-45,0,0,0],30)
C = mc.get_coords()

while True:
    C = mc.get_coords()
    print(C)
    