import sys

from pybricks.ev3devices import Motor, TouchSensor
from pybricks.tools import wait, StopWatch
from pybricks.robotics import DriveBase


def lift_fork(lift_motor):
    lift_motor.run_target(1000, 270)


def lower_lift_fork(lift_motor):
    lift_motor.run_target(100, 0)


def check_pallet(lift_motor, touch_sensor):
    print(has_pallet(touch_sensor))
    if not has_pallet(touch_sensor):
        lower_lift_fork(lift_motor)


def has_pallet(touch_sensor: TouchSensor):
    return touch_sensor.pressed()


def lift(drive_base: DriveBase, lift_motor: Motor, touch_sensor: TouchSensor, height: int = 0) -> bool:
    drive_base.drive(-100, 0)
    time = StopWatch()
    time.reset()

    while not has_pallet(touch_sensor) and time.time() < 4000:
        pass
    backing_time = time.time()
    drive_base.drive(0, 0)

    if backing_time >= 4000:
        return False

    if has_pallet(touch_sensor):
        wait(500)
        lift_fork(lift_motor)

    drive_base.drive(-100, 0)
    time.reset()
    drive_base.drive(100, 0)
    while time.time() < (backing_time-500): #Backar så långt som den körde fram
        pass
    drive_base.drive(0, 0)


if __name__ == '__main__':
    sys.exit(lift())