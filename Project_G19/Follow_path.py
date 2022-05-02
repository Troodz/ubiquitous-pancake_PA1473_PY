
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.parameters import Port, Stop, Direction, Button, Color

def follow_straight_path(drivebase, left_sens, desired_color):
    if left_sens.color() == desired_color:
        drivebase.drive(-60, 40)
    else:
        drivebase.drive(-60, -40)

def obstacle_ahead(drivebase, ultra_sens, ev3):
    if ultra_sens.distance() < 200:
        drivebase.drive(0, 0)
        ev3.speaker.say("Obstacle ahead")
        return True
    return False


def find_desired_path(ev3, drivebase, desired_color, left_sens):
    drivebase.straight(-100)
    while left_sens.color() != desired_color: # snurrar och söker efter färgen
        drivebase.turn(-10)
        drivebase.straight(20)
    return desired_color


"""
def find_desired_path(ev3,drivebase,desired_color,left_sens):
    'hittar desierd path och retunerar desierd color'
    ev3.light.on(desired_color)
    while left_sens.color() != desired_color:
        if left_sens.color() == Color.WHITE:
            drivebase.drive(-50, 40)
        else:
            drivebase.drive(-50, -40)
    return False
"""


