from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.parameters import Port, Stop, Direction, Button, Color

def follow_straight_path(drivebase, left_sens, desired_color, ev3):
    ev3.light.on(desired_color)
    ev3.screen.draw_text(50,50,str(desired_color))
    if left_sens.color() == desired_color:
        drivebase.drive(60, -40)
    else:
        drivebase.drive(60, 40)


def obstacle_ahead(drivebase, ultra_sens, ev3):
    if ultra_sens.distance() < 200:
        drivebase.drive(0, 0)
        ev3.speaker.say("Obstacle ahead")
        return True
    return False


def find_desired_path(ev3, drivebase: DriveBase, desired_color: Color, left_sens: ColorSensor):

    drivebase.straight(100)
    # reverse and turn, try to keep the sensor from moving too much.
    drivebase.drive(-70, 70)
    ev3.screen.draw_text(50, 50, "Turning")
    while left_sens.color() != desired_color:  # snurrar och söker efter färgen
        pass
    drivebase.drive(0, 0)
    ev3.screen.draw_text(50, 50, "Successfully entered a new area")
    return desired_color

#Robert was here
