from djitellopy import Tello
import time

vt = 15

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

    tello.go_xyz_speed( 0, 40, -40, vt)

  time.sleep(3)
  tello.land()
# if "battery too low"