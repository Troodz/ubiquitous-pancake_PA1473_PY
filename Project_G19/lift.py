import sys

from pybricks.ev3devices import Motor, TouchSensor
from pybricks.tools import wait, StopWatch
from pybricks.robotics import DriveBase


def lift_fork(lift_motor):
    lift_motor.run_angle(10, 180)


def lower_lift_fork(lift_motor):
    lift_motor.run_angle(10, -180)


def check_pallet(lift_motor):
    if not has_pallet():
        lower_lift_fork(lift_motor)


def lift_old(drive_base: DriveBase, lift_motor, touch_sensor: TouchSensor, height: int = 0):
    drive_base.drive(100, 0)
    time = StopWatch()
    time.reset()
    while not has_pallet(touch_sensor) and time.time() < 1000:
        pass
    drive_base.drive(0, 0)
    wait(500)
    lift_fork(lift_motor)
    wait(500)
    drive_base.straight(-100)


def has_pallet(touch_sensor: TouchSensor):
    return touch_sensor.pressed()


def lift(drive_base: DriveBase, lift_motor: Motor, touch_sensor: TouchSensor, height: int = 0):
    drive_base.drive(100, 0)
    time = StopWatch()
    time.reset()
    while not has_pallet(touch_sensor) and time.time() < 1000:
        pass
    backing_time = time.time()
    if has_pallet(touch_sensor):
        drive_base.drive(0, 0)
        wait(500)
        lift_fork(lift_motor)
        check_pallet(lift_motor) # kontrollerar om pallen fortfarande är kvar
        wait(500)
    drive_base.drive(-100, 0)
    time = StopWatch()
    time.reset()
    while time.time() < backing_time: #Backar så långt som den körde fram
        pass
    drive_base.drive(0, 0)


if __name__ == '__main__':
    sys.exit(lift())