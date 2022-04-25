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

#lift.lift(drivebase, lift_motor, touch_sensor)

lift_motor.run(100)
time = StopWatch()
time.reset()
while time.time() < 4000:
    pass
lift_motor.run(0)

lift.lift(drivebase, lift_motor, touch_sensor)


while True:
    Follow_path.obstical_check(drivebase, ultra_sens, ev3)
    Follow_path.follow_path(drivebase, left_sens)

