from djitellopy import Tello
import time


S  = 60
W  = 80
W2 = int(W / 2)
H = 70
R = 40


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

    print("get_height")
    print( h )

    time.sleep(3)
    if h > 50:
      tello.go_xyz_speed( 0, 0,  -S, vt)   # T0
      tello.rotate_counter_clockwise(90)
      tello.move_up( H )                   # T1
      time.sleep( 5 )
      tello.move_left( W )                 # T3
      time.sleep( 5 )
      tello.go_xyz_speed( 0, -W, -H, vt)   # T0
      time.sleep( 5 )
      tello.move_left( W )                 # T4
      time.sleep( 5 )
      tello.move_up( H )                   # T3
      time.sleep( 5 )
      tello.go_xyz_speed( 0, -W2,  R, vt)  # T2
      time.sleep( 5 )
      tello.go_xyz_speed( 0, -W2, -R, vt)  # T1
      time.sleep( 5 )
      tello.go_xyz_speed( 0,  W,  -H, vt)  # T4
      time.sleep( 5 )

      tello.rotate_clockwise(90)


  time.sleep(3)
  tello.land()
# if "battery too low"