
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.tools import wait, StopWatch, DataLog

def follow_path(drivebase, left_sens, reflection_threshold):
    if left_sens.reflection() < reflection_threshold:
        drivebase.drive(-50, 40)
    else:
        drivebase.drive(-50, -40)

def obstical_check(drivebase, ultra_sens, ev3):
    if ultra_sens.distance() < 200:
        drivebase.drive(0, 0)
        ev3.speaker.say("Obstical detected")

def multiple_paths(drivebase, ultra_sens, ev3, left_sens):

    reflection_threshold = left_sens.reflection()
    #Gets the first reflection it sees, put on circle line
    DEFAULT_REFLECTION = left_sens.reflection()
    desired_color = "Color.RED"

    wait(100)
    ev3.speaker.beep()
    # Revise - infinite while loops are *illegal*


    while True:
        if left_sens.color() == desired_color and left_sens.reflection != DEFAULT_REFLECTION:
            reflection_threshold = left_sens.reflection()
        
        print("follows path")
        print(reflection_threshold)
        print(left_sens.color())
        follow_path(drivebase, left_sens, reflection_threshold)
        # if left_sens.color() == COLOR_THRESHOLD:
        #     drivebase.drive(DRIVE_SPEED, TURN_SPEED)
        # else:
        #     drivebase.drive(DRIVE_SPEED, -TURN_SPEED)


    # lift functionality
    lift.lift(drivebase, lift_motor, 0)

    return 0


