#!/usr/bin/env pybricks-micropython
from asyncio.windows_events import NULL
import sys
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

import lift


DISTANCE_THRESHOLD = 140
REFLECTION_THRESHOLD = 20
DRIVE_SPEED = 50
TURN_SPEED = 40


def main():
    ev3 = EV3Brick()
    left_wheel = Motor(Port.B)
    right_wheel = Motor(Port.C)
    left_sens = ColorSensor(Port.S3)
    ultra_sens = UltrasonicSensor(Port.S4)
    lift_motor = Motor(Port.A)

    drivebase = DriveBase(left_wheel, right_wheel,
                          wheel_diameter=47, axle_track=128)

    # Heart beat - robot is alive.
    ev3.speaker.beep()
    lift.lift(drivebase, lift_motor, height=NULL)
    # wait(100)
    # ev3.speaker.beep()

    # # Revise - infinite while loops are *illegal*
    # while True:
    #     if ultra_sens.distance() > DISTANCE_THRESHOLD:
    #         if left_sens.reflection() < REFLECTION_THRESHOLD:
    #             drivebase.drive(-DRIVE_SPEED, TURN_SPEED)
    #         else:
    #             drivebase.drive(-DRIVE_SPEED, -TURN_SPEED)

    # lift functionality
    lift.lift(drivebase, lift_motor, 0)

    return 0


if __name__ == '__main__':
    sys.exit(main())
