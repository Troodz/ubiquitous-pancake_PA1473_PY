import sys

from pybricks.ev3devices import Motor, TouchSensor
from pybricks.tools import wait, StopWatch
from pybricks.robotics import DriveBase


def lift_fork(lift_motor):
    lift_motor.track_target(-270)


def lower_lift_fork(lift_motor):
    lift_motor.track_target(0)


def check_pallet(lift_motor, touch_sensor):
    print(has_pallet(touch_sensor))
    if not has_pallet(touch_sensor):
        lower_lift_fork(lift_motor)


def has_pallet(touch_sensor: TouchSensor):
    return touch_sensor.pressed()

def reset_lift(lift_motor):
    lift_motor.run_until_stalled(100)
    lift_motor.reset_angle(0)


def lift(drive_base: DriveBase, lift_motor: Motor, touch_sensor: TouchSensor, height: int = 0) -> bool:
    drive_base.drive(-100, 0)
    time = StopWatch()
    time.reset()

    # Move forward until a pallet is detected or the time has surpassed some time.
    while not has_pallet(touch_sensor) and time.time() < 4000:
        backing_time = time.time()
    drive_base.drive(0, 0)

    # if the time it took to find the pallet is longer than some time then no pallet has been found.
    if backing_time >= 4000:
        return False

    # otherwise if the pallet has been found then lift the fork.
    if has_pallet(touch_sensor):
        wait(500)
        lift_fork(lift_motor)
        wait(500)

    time.reset()
    drive_base.drive(100, 0)
    while time.time() < backing_time: #Backar så långt som den körde fram
        pass
    drive_base.drive(0, 0)

    return True


if __name__ == '__main__':
    sys.exit(lift())