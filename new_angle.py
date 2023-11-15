from pymycobot.mycobot import MyCobot
import pymycobot
from pymycobot import PI_PORT, PI_BAUD 
import time
import os
import sys
from pymycobot.genre import Angle, Coord
import time


mc = MyCobot("COM9", 115200)

def cordsGenrator():
    yield [66.9, -54.2, 405.8, 100.38, 42.4, 105.29]
    yield [-196.5, -56.0, 70.9, -93.2, 57.77, 7.28]
    yield [-203.3, -42.7, 73.8, -93.25, 57.95, 3.52]
    yield [-227.4, -44.9, 70.9, -91.17, 60.28, 5.55]
    yield [-223.3, -59.0, 69.2, -94.09, 59.33, 6.15]
    yield [-225.6, -66.7, 97.7, -91.01, 52.55, 11.35]
    yield [-222.4, -73.8, 81.7, -96.64, 54.64, 8.06]
    yield [-211.1, -72.5, 74.8, -100.99, 47.94, 1.18]
    yield [-237.7, -75.1, 89.5, -110.18, 56.24, -10.37]
    yield [-220.7, -75.6, 92.4, -97.19, 58.19, 6.95]
    yield [-216.5, -83.9, 72.3, -95.29, 57.25, 11.46]
    yield [-207.4, -77.7, 84.6, -110.12, 52.54, -8.58]
    yield [-211.0, -87.9, 85.3, -110.78, 53.01, -4.65]
    yield [-202.7, -97.1, 89.2, -115.05, 49.09, -7.56]

speed = 30
    
for cords in cordsGenrator():
    # mc.send_coords(cords, speed)
    mc.sync_send_coords(cords, speed, 1, timeout=2)
    time.sleep(2)