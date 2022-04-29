#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

ev3 = EV3Brick()
left_wheel = Motor(Port.B)
right_wheel = Motor(Port.C)
lift_motor = Motor(Port.A)
touch_sensor = TouchSensor(Port.S1)
left_sens = ColorSensor(Port.S3)
ultra_sens = UltrasonicSensor(Port.S4)

drivebase = DriveBase(left_wheel, right_wheel,
                        wheel_diameter=47, axle_track=128)

###########################################################

import lift, Follow_path

new_color = Color.BLUE
desired_color = Color.RED

while True:
    Follow_path.follow_straight_path(drivebase, left_sens, desired_color)
    if left_sens.color() == new_color:
        drivebase.straight(-100)
        while left_sens.color() != new_color:
            drivebase.turn(-10)
        desired_color = new_color
        new_color = Color.RED
