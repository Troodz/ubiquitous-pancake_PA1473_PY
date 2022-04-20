#!/usr/bin/env pybricks-micropython

from pybricks.ev3devices import Motor, ColorSensor, UltrasonicSensor
from pybricks.parameters import Port, Direction, Button
from pybricks.tools import wait
from pybricks.hubs import EV3Brick
from pybricks.robotics import DriveBase



left_motor = Motor(Port.C)#kan vara omvänt
right_motor = Motor(Port.B)#ingen aning faktiskt vilken port som är vad jag hittar bara på
forklift = Motor(Port.A, positive_direction=Direction.CLOCKWISE, gears=[12, 20])
line_sensor = ColorSensor(Port.S3)
cruise_sensor = UltrasonicSensor(Port.S4)
robot = DriveBase(left_motor, right_motor, wheel_diameter=47, axle_track=128)

stopping_distance = 150

# def drive():

#     BLACK = 9
#     WHITE = 85
#     threshold = (BLACK + WHITE) / 2

#     DRIVE_SPEED = 100

#     PROPORTIONAL_GAIN = 1.2
#     right_motor.dc(-50)
#     left_motor.dc(-50)
#     while True:

#         if line_sensor().reflection >80:
#             left_motor(-50)
#             right_motor(25)
#         else:
#             left_motor(-50)
#             right_motor(25)
        # # Calculate the deviation from the threshold.
        # deviation = line_sensor.reflection() - threshold

        # # Calculate the turn rate.
        # turn_rate = PROPORTIONAL_GAIN * deviation

        # # Set the drive base speed and turn rate.
        # robot.drive(DRIVE_SPEED, turn_rate)

        # You can wait for a short time or do other things in this loop.
        # right_motor.dc(-50)
        # left_motor.dc(-50)
        #robot.drive(50, 0)
        #print(line_sensor.color())
        #print(cruise_sensor.distance())


# def lift():
#     while(True):
#         forklift.run_until_stalled(speed, then=Stop.COAST, duty_limit=None)

def drive():
    ev3 = EV3Brick()
    while True:

        print(line_sensor.ambient())
        if line_sensor.ambient() > 4:
            right_motor.dc(-50)
            left_motor.dc(25)
            wait(15)

        else:
            left_motor.dc(-50)
            right_motor.dc(25)
            wait(15)
        left_motor.dc(-50)
        right_motor.dc(-50)

        if Button.DOWN in ev3.buttons.pressed():
            left_motor.dc(0)
            right_motor.dc(0)

            wait(5000)
    #robot.drive(-50, 25)




drive()


# def brown():

# def red():

# def blue():

# def green():

#main()
# while(True):
#     obstacel_distance = cruise_sensor.distance()
#     current_line = line_sensor.color()

#     if obstacle_distance < stopping_distance:

#         drive()
#         if(current_line == color.yellow)
#             break

#         elif current_line = color.brown:
#             brown()

#         elif current_line = color.red:
#             red()

#         elif current_line = color.blue:
#             blue()

#         elif current_line = color.green:
#             green()
#     else:
#         wait(5)