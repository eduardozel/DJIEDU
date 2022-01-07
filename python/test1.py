from djitellopy import Tello
import time


tello = Tello()
tello.connect()
battery = tello.get_battery()
print( battery )

if battery < 10:
  print( "battery too low")
else:
  tello.takeoff()
  if tello.is_flying:
    print(">Flying")
    h = tello.get_height()
    print("get_height ->")
    print( h )
    tello.move_down( h - 20 )

  time.sleep(3)
  tello.land()
# if "battery too low"