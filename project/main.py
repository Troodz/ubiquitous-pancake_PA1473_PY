#!/usr/bin/env pybricks-micropython
import sys
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

import Run_path, lift


def main():
    ev3 = EV3Brick()
    left_wheel = Motor(Port.B)
    right_wheel = Motor(Port.C)
    left_sens = ColorSensor(Port.S3)
    ultra_sens = UltrasonicSensor(Port.S4)
    lift = Motor(Port.A)

    drivebase = DriveBase(left_wheel, right_wheel, wheel_diameter = 47, axle_track = 128)

    # This program requires LEGO EV3 MicroPython v2.0 or higher.
    # Click "Open user guide" on the EV3 extension tab for more information.


    # Create your objects here.
    ev3 = EV3Brick()
    # RÖR EJ OVAN

    # Write your program here.
    ev3.speaker.beep()

    wait(100)

    ev3.speaker.beep()

    while True:
        #Run_path.follow_path()
        if left_sens.reflection() < 20:
            drivebase.drive(-50, 40)
        else:
            drivebase.drive(-50, -40)

    lift.lift(robotDB, lift_motor, 0)

    # RÖR EJ
    wait(10000)
    ev3.speaker.beep()
    return 0

if __name__ == '__main__':
    sys.exit(main())