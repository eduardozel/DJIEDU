from djitellopy import Tello
import time


tello = Tello()

tello.connect()
battery = tello.get_battery()
print( battery )
tello.turn_motor_on
print( "time" )
time.sleep(5)
print( "off" )
tello.turn_motor_off
response = tello.takeoff()
print(response)
time.sleep(3)
tello.land()
