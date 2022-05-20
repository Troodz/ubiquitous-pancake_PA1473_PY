#!/usr/bin/env pybricks-micropython
#Libaries
import math
#EV3
from pybricks.ev3devices import Motor, ColorSensor, UltrasonicSensor, TouchSensor, InfraredSensor
from pybricks.parameters import Port, Direction, Button, Color, Stop
from pybricks.tools import wait
from pybricks.hubs import EV3Brick
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import Font
#Python

#Definitons
left_motor = Motor(Port.B)#kan vara omvänt
right_motor = Motor(Port.C)#ingen aning faktiskt vilken port som är vad jag hittar bara på
forklift = Motor(Port.A, positive_direction=Direction.CLOCKWISE, gears=[12, 36])
line_sensor = ColorSensor(Port.S3)
cruise_sensor = UltrasonicSensor(Port.S4)

robot = DriveBase(left_motor, right_motor, wheel_diameter=47, axle_track=128)
touch_sensor = TouchSensor(Port.S1)
#Variables
run_statement = True
instructions = False
#Parameters
maxdistance = 3.0 # May need to calibrate
stopping_distance = 300
working_speed = 100
move_speed = -80

ev3 = EV3Brick()

def lift(up_down, angle):
    '''Lifting up/down on angle'''
    ev3.light.on(Color.YELLOW)
    msg("Lifting "+str(up_down))
    forklift.run_target(working_speed*up_down, angle, then=Stop.HOLD, wait=True)
    ev3.light.on(Color.GREEN)
    msg("Done")
    return True

def lift_until_pressed():
    '''Driving towars pallet until button is pressed'''
    lift(-1, -5)
    right_motor.dc(-50)
    left_motor.dc(-50)
    msg("Will try to lift")
    while(not touch_sensor.pressed()):
        wait(10)
    right_motor.dc(0)
    left_motor.dc(0)
    lift(1, -50)
    right_motor.dc(50)
    left_motor.dc(50)
    wait(2000)
    right_motor.dc(0)
    left_motor.dc(0)
    msg("Done")
def reset_clow():
    '''Reseting claw'''
    msg("Reseting claw")
    forklift.run_until_stalled(working_speed, then=Stop.COAST, duty_limit=None)
    forklift.reset_angle(0)
    ev3.screen.clear()

def elevated_surface(direction):
    '''Gathering pallet from elevated surface'''
    lift(-1, -5)
    forklift.run_target(working_speed*direction, -67, then=Stop.HOLD, wait=True)
    left_motor.dc(-50)
    right_motor.dc(-50)
    while(not touch_sensor.pressed()):
        wait (10)
    right_motor.dc(0)
    left_motor.dc(0)
    lift(1, -90)
    right_motor.dc(50)
    left_motor.dc(50)
    wait(2000)
    lift(-1, -67)
    right_motor.dc(0)
    left_motor.dc(0)

# def detect_color(AvalibleColors):
#     '''Calculating color'''
#     currentRGB = line_sensor.rgb()
#     currentColor = " "
#     bestDistance = 0.0
#     for i in range(0, len(AvalibleColors)):
#         #print(AvalibleColors[list(AvalibleColors.keys())[0]][0])
#         r = AvalibleColors[list(AvalibleColors.keys())[i]][0] - currentRGB[0]
#         g = AvalibleColors[list(AvalibleColors.keys())[i]][1] - currentRGB[1]
#         b = AvalibleColors[list(AvalibleColors.keys())[i]][2] - currentRGB[2]
#         distance = math.sqrt(abs((r)^2 + (g)^2 + (b)^2))
#         if distance < maxdistance and distance < bestDistance or bestDistance == 0: # Giving the color detection some room
#             currentColor = list(AvalibleColors.keys())[i]
#             bestDistance = distance
#         else:
#             pass
#     return currentColor
#
# def follow_line(line_color, backround):
#     '''Following line using reflection'''
#     turn_ration = 10.5
#     current_line = line_sensor.reflection()
#     perfect_line = (line_color + backround) / 2
#     robot.drive(move_speed, (perfect_line - current_line) * turn_ration)


def follow_line(line_color, avalible_colors):
    '''Following line using color'''
    current_line = get_current_color(avalible_colors)
    if current_line != line_color:
        right_motor.dc(-50)
        left_motor.dc(25)
        wait(15)
#140 -5 < 145 > +5 150
    else:
        left_motor.dc(-50)
        right_motor.dc(25)
        wait(15)

        #left_motor.dc(-50)
        #right_motor.dc(-50)

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
    '''Getting distace data'''
    return cruise_sensor.distance()

def avoid_collison():
    '''Stopping for object'''
    robot.stop()A
    left_motor.dc(0)
    right_motor.dc(0)
    ev3.light.on(Color.RED)
    while obstacle_distance() < stopping_distance:
        wait(10)

    ev3.light.on(Color.GREEN)

def paralysed():
    '''Just freezing robot'''
    robot.stop()
    left_motor.dc(0)
    right_motor.dc(0)
def get_instructions():
    '''Getting instructions for the route'''

    msg("Choose 3 colors")
    instructions = []

    while len(instructions) != 3:
        if Button.DOWN in ev3.buttons.pressed():
            instructions.append((line_sensor.rgb()[0], line_sensor.rgb()[1], line_sensor.rgb()[2], line_sensor.reflection()))
            print(instructions)
            wait(1000)

    print(instructions)
    ev3.screen.clear()
    return instructions
def calculate_RGB_HSV(color):
    #Making the range for the color spectrum variate between 0 and 1
    r = color[0] / 255.0
    g = color[1] / 255.0
    b = color[2] / 255.0
    #Finding out which of the three rgb scales which is highest and which is lowest
    currentMin = min(r, g, b)   
    currentMax = max(r, g, b)    
    v = currentMax * 100
    difference = currentMax-currentMin       
 
    #If tge differenc between the colors are the same then there is not a big coler difference and therfor hue is equal to zero
    if currentMax == currentMin:
        h = 0
    # Calculating HUE depending on which color had the highest value 
    elif currentMax == r:
        h = (60 * ((g - b) / difference) + 360) % 360
 
   
    elif currentMax == g:
        h = (60 * ((b - r) / difference) + 120) % 360
 
    elif currentMax == b:
        h = (60 * ((r - g) / difference) + 240) % 360
 
    #Calculating Saturation which describes how much of a color is shown 
    if currentMax == 0:
        s = 0
    else:
        s = (difference / currentMax) * 100
 
   
    return h, s, v

 

def get_avalible_colors():
    '''Gattering colors'''
    #hej[list(hej.keys())[0]]
    colors = ["YELLOW", "BLUE", "PINK", "PURPLE", "BACKROUND"]
    colorsRGB = []
    msg(colors[0])
    pressed = 0
    while len(colorsRGB) != 5:


        if Button.CENTER in ev3.buttons.pressed():
            if len(colorsRGB) + 1 != 5:
                msg(colors[len(colorsRGB)+ 1])
            colorsRGB.append([colors[pressed], sum(calculate_RGB_HSV(line_sensor.rgb()))])
            
            wait(1000)
            pressed = pressed + 1
  
    return colorsRGB
def timer(start_time, text):
    '''Counter which displays'''
    for i in range(start_time, 0, -1):
        msg(text + str(i))
        wait(1000)


def msg(text):
    '''Printer'''
    ev3.screen.clear()
    #fontSize = Font(24 - len(text) + 3)
    #ev3.screen.set_font(size=6)
    ev3.screen.draw_text(20, 50, text)

def get_current_color(avalible):
    SHSV = sum(calculate_RGB_HSV(line_sensor.rgb()))
    old_diff = 0
    #print(avalible[0][1])
    for i in range(0, len(avalible)):
        
        difference = abs(SHSV - avalible[i][1])
        if difference < old_diff or old_diff == 0:
            current_color = avalible[i][0]
            old_diff = difference
    return current_color

def test():
    '''Testing facility'''
    msg("Resetig robot")
    robot.reset()
    reset_clow()
    wait(1000)
    timer(5, "test begins in ")
    timer(5, "90 degree to right")
    robot.turn(90)
    timer(5, "90 degree to left")
    robot.turn(-180)
    timer(5, "lift test in ")

    lift(1, -67)
    timer(5, "elevated test in ")
    elevated_surface(1)
    timer(5, "ground test in ")
    lift_until_pressed()
if __name__ == "__main__":
    '''MAIN FUNCTION'''
    #Variables in use
    current_step = 0
    instruction_list = []
    avalible_colors = []
    current_reflection = 3
    reset_clow()
    current_color = None

    while(run_statement): #Drive loop


        # if obstacle_distance() < stopping_distance:
        #     avoid_collison()

        if instructions == False:
            paralysed()
            #instruction_list = get_instructions()
            instruction_list = ["YELLOW", "BLUE", "PINK"]
            avalible_colors = get_avalible_colors()
            current_color = "YELLOW"
            instructions = True


        else:
           
           
            current_color = follow_line(instruction_list[current_step], avalible_colors)
            print(current_color)
            if current_color == instruction_list[current_step + 1]:
                print("Changes color")
                
                current_step = current_step + 1
                #current_reflection = line_sensor.reflection()
                if current_step == len(instruction_list)-1:
                    current_step = 0

                    instruction_list.reverse()
