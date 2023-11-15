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
import csv
import threading
import keyboard




mc = MyCobot("COM10", 115200)
time.sleep(2)

time.sleep(2)
mc.release_all_servos()
x="y"
A=[]
i=0
j=0
while True:
        a=mc.get_coords()
        A.append(a)
        print(a)
        time.sleep(1)
        i=0
        if keyboard.is_pressed('n'):
            while True:
                mc.sync_send_coords(A[i],30)
                i=i+1
    
    
    
    
    

