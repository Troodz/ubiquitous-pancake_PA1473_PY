#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

motor_direction = Direction.COUNTERCLOCKWISE

ev3 = EV3Brick()
left_wheel = Motor(Port.B, positive_direction=motor_direction)
right_wheel = Motor(Port.C, positive_direction=motor_direction)
lift_motor = Motor(Port.A, gears=(12,36), positive_direction=Direction.COUNTERCLOCKWISE)
touch_sensor = TouchSensor(Port.S1)
left_sens = ColorSensor(Port.S3)
ultra_sens = UltrasonicSensor(Port.S4)

drivebase = DriveBase(left_wheel, right_wheel,
                        wheel_diameter=47, axle_track=128)

###########################################################

while True:
    print(left_sens.color())
    wait(1000)