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
left_wheel = Motor(Port.B)
right_wheel = Motor(Port.C)
left_sens = ColorSensor(Port.S3)
ultra_sens = UltrasonicSensor(Port.S4)
turn_sens = 30
run_rate = 200
# spkr = Sound()
robot = DriveBase(left_wheel, right_wheel, wheel_diameter = 56, axle_track = 118)

# Write your program here.
    # ------------ Uppg2
def go_robot_go(i):
    left_wheel.run(200*i)
    right_wheel.run(200*i)

def run_run_left():
    right_wheel.run(150)
    left_wheel.run(40)

def run_run_right():
    left_wheel.run(150)
    right_wheel.run(40)

def whole_turn(i):
    left_wheel.run(-200*i)
    right_wheel.run(200*i)

def stop():
    left_wheel.run(0)
    right_wheel.run(0)

while True:
    # Testar ifall något är ivägen 
    if ultra_sens.distance() < 140.0: # Något ivägen
        counter = 0
        print("Oh nej, något är ivägen")
        stop()
        ev3.speaker.say("Obsticle is in the way")
    else: # Inget ivägen
        if left_sens.reflection() > turn_sens:
            if left_sens.reflection() > 20 and left_sens.reflection() < 30:
                go_robot_go(1)
            elif left_sens.reflection() < 20:
                run_run_right()
            elif left_sens.reflection() > 30:
                run_run_left()
                

