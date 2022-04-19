from pybricks.ev3devices import Motor, TouchSensor
from pybricks.tools import wait, StopWatch
from pybricks.robotics import DriveBase

def lift(drive_base: DriveBase, lift_motor: Motor, height: int):
    drive_base.drive(100, 0)
    time = StopWatch()
    time.reset() 
    while not has_pallet() and time.time() < 1000:
        pass
    drive_base.drive(0, 0)
    wait(500)
    lift_motor.run_angle(10, 5)
    wait(500)
    drive_base.straight(-100)

def has_pallet(touch_sensor: TouchSensor):
    return touch_sensor.pressed()