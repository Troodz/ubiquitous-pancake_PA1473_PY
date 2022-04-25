
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.tools import wait, StopWatch, DataLog

def follow_path(drivebase, left_sens):
    if left_sens.reflection() < 20:
        drivebase.drive(-50, 40)
    else:
        drivebase.drive(-50, -40)

def obstical_check(drivebase, ultra_sens, ev3):
    if ultra_sens.distance() < 200:
        drivebase.drive(0, 0)
        ev3.speaker.say("Obstical detected")

def multiple_paths(drivebase, ultra_sens, ev3, left_sens):

    DISTANCE_THRESHOLD = 140
    REFLECTION_THRESHOLD = ColorSensor.reflection()
    #Gets the first reflection it sees, put on circle line
    DEFAULT_REFLECTION = ColorSensor.reflection()
    DRIVE_SPEED = 50
    TURN_SPEED = 40
    desired_color = 1

    wait(100)
    ev3.speaker.beep()
    # Revise - infinite while loops are *illegal*
    while True:
        if ultra_sens.distance() > DISTANCE_THRESHOLD:
            if left_sens.color() == desired_color and left_sens.reflection != DEFAULT_REFLECTION:
                REFLECTION_THRESHOLD = left_sens.reflection()
            elif left_sens.reflection() < REFLECTION_THRESHOLD:
                drivebase.drive(-DRIVE_SPEED, TURN_SPEED)
            else:
                drivebase.drive(-DRIVE_SPEED, -TURN_SPEED)
            # if left_sens.color() == COLOR_THRESHOLD:
            #     drivebase.drive(DRIVE_SPEED, TURN_SPEED)
            # else:
            #     drivebase.drive(DRIVE_SPEED, -TURN_SPEED)


    # lift functionality
    lift.lift(drivebase, lift_motor, 0)

    return 0


