#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.

# Create your objects here.
ev3 = EV3Brick()

# Write your program here.
ev3.speaker.beep()

#############################################################

# Våra importer
import lift, Follow_path, ware_house

motor_direction = Direction.COUNTERCLOCKWISE

ev3 = EV3Brick()
left_wheel = Motor(Port.B, positive_direction=motor_direction)
right_wheel = Motor(Port.C, positive_direction=motor_direction)
lift_motor = Motor(Port.A, gears=(12,36), positive_direction=Direction.CLOCKWISE)
touch_sensor = TouchSensor(Port.S1)
left_sens = ColorSensor(Port.S3)
ultra_sens = UltrasonicSensor(Port.S4)

drivebase = DriveBase(left_wheel, right_wheel,
                        wheel_diameter=47, axle_track=128)


ev3.speaker.beep()
# roboten startar

reflection_threshold = 0
current_color = Color.BROWN
obstacle_detected = False
in_warehouse = False
found=True
lifted = False ## Lägg in lifted funktion som returnerar bool

color_queue = [Color.RED, Color.BROWN]

def get_color(queue: list[Color]) -> Color:
    tmp = queue[0]
    queue.remove(queue[0])
    queue.append(tmp)
    return tmp

desired_color = get_color(color_queue)

lift.reset_lift(lift_motor)

while True:
    # print("pallet ahead: ", ware_house.pallet_ahead(drivebase, ultra_sens))
    # print("Obstacle detected: ", obstacle_detected)
    # print("is lifting: ", lifted)
    #print("obstacle detected", obstacle_detected)
    
    if not lifted and not in_warehouse:
        obstacle_detected = Follow_path.obstacle_ahead(drivebase, ultra_sens, ev3)
    if in_warehouse:
        if ware_house.pallet_ahead(drivebase, ultra_sens) and not lifted:
            lifted = lift.lift(drivebase, lift_motor, touch_sensor)
    if not obstacle_detected:
        if left_sens.color() == desired_color:
            current_color = Follow_path.find_desired_path(ev3, drivebase, desired_color, left_sens)
            desired_color = get_color(color_queue)
    
    if current_color == Color.RED:
        in_warehouse = True

    

    print("Current color:", current_color)
    print("Sens", left_sens.color())
    Follow_path.follow_straight_path(drivebase, left_sens, current_color)
