from pybricks.ev3devices import Motor, TouchSensor
from pybricks.tools import wait
from pybricks.robotics import DriveBase

def lift(drive_base: DriveBase, lift_motor: Motor, height: int):
    drive_base.straight(100)
    wait(500)
    lift_motor.run_angle(10, 5)
    wait(500)
    drive_base.straight(-100)

def has_pallet(touch_sensor: TouchSensor):
    return touch_sensor.pressed()