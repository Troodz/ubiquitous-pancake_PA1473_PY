#!/usr/bin/env pybricks-micropython
#Libaries
#EV3
from pybricks.ev3devices import Motor, ColorSensor, UltrasonicSensor, TouchSensor
from pybricks.parameters import Port, Direction, Button, Color, Stop
from pybricks.tools import wait
from pybricks.hubs import EV3Brick
from pybricks.robotics import DriveBase
#Python

#Definitons
left_motor = Motor(Port.C)#kan vara omvänt
right_motor = Motor(Port.B)#ingen aning faktiskt vilken port som är vad jag hittar bara på
forklift = Motor(Port.A, positive_direction=Direction.CLOCKWISE, gears=[12, 20])
line_sensor = ColorSensor(Port.S3)
cruise_sensor = UltrasonicSensor(Port.S4)
robot = DriveBase(left_motor, right_motor, wheel_diameter=47, axle_track=128)
touch_sensor = TouchSensor(Port.S1)
#Variables
stopping_distance = 150
working_speed = 50
move_speed = -50
run_statement = True
instructions = True
ev3 = EV3Brick()

def lift(up_down):
    ev3.light.on(Color.YELLOW)
    while(True):
        #forklift.run_until_stalled(working_speed*up_down, then=Stop.COAST, duty_limit=None)
        forklift.run_angle(working_speed*up_down, 60, then=Stop.HOLD, wait=True)
    return True

# def lift_until_pressed(touch_sensor):
#     touch_sensor.pressed()
#     while(False):



def follow_line(line_color, forklift):
    '''This function will make the robot follow a selected line color'''
    current_line = line_sensor.color()
    if current_line != line_color:
        right_motor.dc(-50)
        left_motor.dc(25)
        wait(15)

    else:
        left_motor.dc(-50)
        right_motor.dc(25)
        wait(15)

        left_motor.dc(-50)
        right_motor.dc(-50)

    return current_line

def user_controll():
    '''This functions waits for the user to make a active decision regarding somthing the robot can't'''
    ev3.light.on(Color.BLUE)
    while not Button.DOWN in ev3.buttons.pressed():
            left_motor.dc(0)
            right_motor.dc(0)
    ev3.light.on(Color.GREEN)
    return True

def obstacle_distance():
    return cruise_sensor.distance()

def avoid_collison(robot):
    #robot.stop()
    left_motor.dc(0)
    right_motor.dc(0)
    ev3.light.on(Color.RED)
    while obstacle_distance() < stopping_distance:
        wait(10)

    ev3.light.on(Color.GREEN)

def paralysed(robot):
    #robot.stop()
    left_motor.dc(0)
    right_motor.dc(0)
def get_instructions():
    '''hhf'''

if __name__ == "__main__":

    #left_motor.dc(-50)
    #right_motor.dc(-50)
    lift(1)
    while(run_statement):
        if obstacle_distance() < stopping_distance:
            avoid_collison(ev3)
        if instructions == False:
            paralysed()
            instruction_list = get_instructions()
ll