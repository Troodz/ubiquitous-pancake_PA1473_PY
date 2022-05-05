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
forklift = Motor(Port.A, positive_direction=Direction.CLOCKWISE, gears=[12, 36])
line_sensor = ColorSensor(Port.S3)
cruise_sensor = UltrasonicSensor(Port.S4)
robot = DriveBase(left_motor, right_motor, wheel_diameter=47, axle_track=128)
touch_sensor = TouchSensor(Port.S1)
#Variables
stopping_distance = 300
working_speed = 100
move_speed = -50
run_statement = True
instructions = False
circulation_color = Color.BLACK
Start_color = Color.GREEN

ev3 = EV3Brick()

def lift(up_down, angle):
    ev3.light.on(Color.YELLOW)
    #forklift.run_until_stalled(working_speed*up_down, then=Stop.HOLD, duty_limit=None)
    forklift.run_target(working_speed*up_down, angle, then=Stop.HOLD, wait=True)
    ev3.light.on(Color.GREEN)
    return True

def lift_until_pressed():

    right_motor.dc(-50)
    left_motor.dc(-50)
    while(not touch_sensor.pressed()):
        wait(10)
    right_motor.dc(0)
    left_motor.dc(0)
    lift(-1, 50)
def reset_clow():
    forklift.run_until_stalled(working_speed, then=Stop.COAST, duty_limit=None)
    forklift.reset_angle(0)

def elevated_surface(direction):
    forklift.run_target(working_speed*direction, -67, then=Stop.HOLD, wait=True)
    left_motor.dc(-50)
    right_motor.dc(-50)
    while(not touch_sensor.pressed()):
        wait (10)
    right_motor.dc(0)
    left_motor.dc(0)
    lift(-1, -90)
    right_motor.dc(50)
    left_motor.dc(50)
    wait(2000)
    lift(1, -67)

def follow_line(line_color):
    '''This function will make the robot follow a selected line color'''
    current_line = line_sensor.color()
    if current_line != line_color:
        right_motor.dc(-50)
        left_motor.dc(25)
        wait(15)
#140 -5 < 145 > +5 150
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

def avoid_collison():
    #robot.stop()
    left_motor.dc(0)
    right_motor.dc(0)
    ev3.light.on(Color.RED)
    while obstacle_distance() < stopping_distance:
        wait(10)

    ev3.light.on(Color.GREEN)

def paralysed():
    #robot.stop()
    left_motor.dc(0)
    right_motor.dc(0)
def get_instructions():
    '''Getting instructions'''
    #RondellButton.DOWN in ev3.buttons.pressed():
    ev3.screen.draw_text(40, 50, "Choose 3 colors")
    my_list = []
    pressed = 0
    while len(my_list) != 3:
        if Button.DOWN in ev3.buttons.pressed():
            my_list.append(line_sensor.color())
            print(my_list)
            wait(1000)

    print(my_list)
    return my_list #[Start_color, circulation_color, Color.BLUE]

if __name__ == "__main__":
    #Variables in use
    current_step = 0
    instruction_list = []
    reset_clow()
    #check_colors()
    while(run_statement):


        if obstacle_distance() < stopping_distance:
            avoid_collison()
            pass
        if instructions == False:
            paralysed()
            instruction_list = get_instructions()
            instructions = True

        else:
            current_color = follow_line(instruction_list[current_step])
            print(f"{current_color} {current_step}")
            if current_color == instruction_list[current_step + 1]:
                current_step = current_step + 1
                if current_step == len(instruction_list)-1:
                    current_step = 0

                    instruction_list.reverse()
