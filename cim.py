from pymycobot.mycobot import MyCobot
import pymycobot
from pymycobot import PI_PORT, PI_BAUD 
import time
import os
import sys
from pymycobot.genre import Angle, Coord
import time


mc = MyCobot("COM7", 115200)

def cordsGenrator():
    k=[[-139.4, 184.4, 101.8, 104.03, 59.04, -161.36],[-144.1, 183.6, 102.2, 102.49, 53.04, -159.07],[-143.5, 163.4, 110.2, 111.52, 52.8, -150.43],[-136.1, 162.9, 110.7, 112.19, 55.84, -155.35]]
    for i in range(k):
        yield k[i] 
   

speed = 40
    
for cords in cordsGenrator():
    # mc.send_coords(cords, speed)
    mc.sync_send_coords(cords, speed, 1, timeout=2)
    time.sleep(2)
