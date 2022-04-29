
from pickle import TRUE
from numpy import true_divide
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.parameters import Port, Stop, Direction, Button, Color

def follow_straight_path(drivebase, left_sens, desired_color):
    if left_sens.color() == desired_color:
        drivebase.drive(-50, 40)
    else:
        drivebase.drive(-50, -40)

def obstical_ahead(drivebase, ultra_sens, ev3):
    if ultra_sens.distance() < 200:
        drivebase.drive(0, 0)
        ev3.speaker.say("Obstical ahead")
        return True
    return False

def multiple_paths(drivebase, ultra_sens, ev3, left_sens):

    reflection_threshold = left_sens.reflection()
    DEFAULT_REFLECTION = left_sens.reflection()
    wait(100)
    ev3.speaker.beep()
    checker=True
    follow_straight_path(drivebase, left_sens, reflection_threshold)
    while checker:
        print(left_sens.color())
        if left_sens.color() == Color.RED and left_sens.reflection != DEFAULT_REFLECTION:
            reflection_threshold = left_sens.reflection()
            checker=False
    print("follows path", reflection_threshold,left_sens.color())
    follow_straight_path(drivebase, left_sens, reflection_threshold)



def find_desired_path(drivebase,desired_color,left_sens):
    go =TRUE
    while go:
        if left_sens.color() == Color.WHITE :
            drivebase.drive(-50, 40)
        else:
            drivebase.drive(-50, -40)
            if left_sens.color() == desired_color:
                drivebase.drive(0,0)
                go = False
    #follow_straight_path(drivebase, left_sens, desired_color)
    return desired_color
