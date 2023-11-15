from pymycobot.mycobot import MyCobot
import time

# Initialize a MyCobot object 
mc = MyCobot("COM11", 115200)

# Turn on the suction pump, note: use one of pins 2 and 5 to control the switch of the suction pump
def pump_on():
    # Let bit 2 work
    mc.set_basic_output(2, 0)
    # Let bit 5 work
    #mc.set_basic_output(5, 0)

# Stop suction pump
def pump_off():
    # Make position 2 stop working
    mc.set_basic_output(2, 1)
    # Make position 5 stop working
    #mc.set_basic_output(5, 1)


mc.release_all_servos()
time.sleep(4)
mc.send_coords( [-235.8, 57.8, 251.8, -2.81, 40.81, -93.73],30)
time.sleep(2)
mc.send_coords( [-67.8, -25.3, 396.7, -81.4, 49.87, -135.8],30)
time.sleep(2)
mc.send_coords(  [-15.0, -79.5, 406.2, -87.98, 45.85, -136.27],30)
time.sleep(4)
pump_on()
time.sleep(2)
mc.send_coords(  [-124.9, -85.4, 322.2, -73.92, 40.16, -71.94],30)
time.sleep(2)
mc.send_coords( [55.0, -66.3, 341.2, -90.0, 45.0, -92.37],30)
time.sleep(4)
pump_off()
time.sleep(2)
mc.send_coords([-80.0, -80.8, 324.0, -70.41, 44.16, -73.6],30)
mc.sleep(2)
pump_off()

pump_off()
time.sleep(3)
pump_on()
time.sleep(3)
pump_off()
time.sleep(3)