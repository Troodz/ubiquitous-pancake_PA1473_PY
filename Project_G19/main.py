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
import lift, Follow_path

ev3 = EV3Brick()
left_wheel = Motor(Port.B)
right_wheel = Motor(Port.C)
lift_motor = Motor(Port.A)
touch_sensor = TouchSensor(Port.S1)
left_sens = ColorSensor(Port.S3)
ultra_sens = UltrasonicSensor(Port.S4)

drivebase = DriveBase(left_wheel, right_wheel,
                        wheel_diameter=47, axle_track=128)

wait(100)
ev3.speaker.beep()
# roboten startar

reflection_threshold = 0
desired_color = Color.RED
obstacle_detected = False
should_lift = False

while True:
    lifted = False ## Lägg in lifted funktion som returnerar bool
    if lifted == False:
        obstacle_detected = Follow_path.obstacle_ahead(drivebase, ultra_sens, ev3)
    if obstacle_detected == False:
        Follow_path.follow_straight_path(drivebase, left_sens, reflection_threshold, desired_color)
        #Follow_path.multiple_paths(drivebase, ultra_sens, ev3, left_sens)
    if should_lift:
        lifted = lift.lift(drivebase, lift_motor, touch_sensor)
