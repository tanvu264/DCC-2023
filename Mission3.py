from djitellopy import tello
import time
tello = tello.Tello()

tello.connect()
tello.takeoff()

tello.rotate_counter_clockwise(45)

for i in range(4):
    tello.move_forward(100)
    tello.rotate_counter_clockwise(90)

tello.land()