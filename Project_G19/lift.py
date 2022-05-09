import sys

from pybricks.ev3devices import Motor, TouchSensor
from pybricks.tools import wait, StopWatch
from pybricks.robotics import DriveBase

import math

def get_lift_angle(height: float, 
        fork_height: int = 3.5, 
        joint_height: int = 10.25, 
        arm_length: float = 13.5, 
        angle_offset: float = -30):
    return math.degrees(math.asin((height + fork_height - joint_height)/arm_length)-math.radians(angle_offset))

def lift_fork(lift_motor):
    lift_motor.track_target(60)


def lower_lift_fork(lift_motor):
    lift_motor.run_angle(50, 0)


def check_pallet(lift_motor, touch_sensor):
    print(has_pallet(touch_sensor))
    if not has_pallet(touch_sensor):
        lower_lift_fork(lift_motor)


def has_pallet(touch_sensor: TouchSensor):
    return touch_sensor.pressed()

def reset_lift(lift_motor):
    lift_motor.run_until_stalled(-100)
    lift_motor.reset_angle(-15)

def check_if_can_lift_pallet(before, after):
    if (after-before) < 10:
        return False
    return True
    
def return_back(drive_base: DriveBase, duration):
    time = StopWatch()
    time.reset()
    drive_base.drive(-100, 0)
    while time.time() < duration: #Backar så långt som den körde fram
        pass
    drive_base.drive(0, 0)


def lift(drive_base: DriveBase, lift_motor: Motor, touch_sensor: TouchSensor, height: int = 0) -> bool:
    drive_base.drive(100, 0)
    time = StopWatch()
    time.reset()

    # Move forward until a pallet is detected or the time has surpassed some time.
    backing_time = time.time()
    while not has_pallet(touch_sensor) and time.time() < 4000:
        backing_time = time.time()
    backing_time -= 500 # magic number otherwise robot backs too much
    drive_base.drive(0, 0)

    # otherwise if the pallet has been found then lift the fork.
    if has_pallet(touch_sensor):
        wait(500)
        start_angel = lift_motor.angle()
        lift_fork(lift_motor)
        end_angle = lift_motor.angle()
        can_lift = check_if_can_lift_pallet(start_angel, end_angle)
        print(can_lift)
        wait(500)
    
    # if the time it took to find the pallet is longer than some time then no pallet has been found.
    if backing_time >= 4000 or not can_lift:
        reset_lift(lift_motor)
        return_back(drive_base, backing_time)
        return False

    return_back(drive_base, backing_time)

    return True


if __name__ == '__main__':
    sys.exit(lift())