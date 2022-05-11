# hej = {}



# hej["Red"] = (255, 0 ,0)

# hej["Blå"] = (0, 0, 255)
# print()
# print(hej[list(hej.keys())[0]])
# print(list(hej.keys())[1])
#print(hej[])
#print(hej[hej.keys()[0]])
import math
AvalibleColors = {}
AvalibleColors["RED"] = (255, 0, 0)
AvalibleColors["BLUE"] = (0, 0, 255)
AvalibleColors["GREEN"] = (0, 255, 0)
maxdistance = 5.0
def detect_color(AvalibleColors):
    '''Calculating color'''
    currentRGB = (255, 0, 100)
    currentColor = " "
    bestDistance = 0.0
    for i in range(0, 3):
        #print(AvalibleColors[list(AvalibleColors.keys())[0]][0])
        r = AvalibleColors[list(AvalibleColors.keys())[i]][0] - currentRGB[0]
        g = AvalibleColors[list(AvalibleColors.keys())[i]][1] - currentRGB[1]
        b = AvalibleColors[list(AvalibleColors.keys())[i]][2] - currentRGB[2]
        distance = math.sqrt(abs((r)^2 + (g)^2 + (b)^2))
        print(distance)
        if distance < maxdistance and distance < bestDistance or bestDistance == 0: # Giving the color detection some room
            currentColor = list(AvalibleColors.keys())[i]
            bestDistance = distance
        else:
            pass
    return currentColor

print(detect_color(AvalibleColors))



def detect_color(AvalibleColors):
    '''Calculating color'''
    currentRGB = line_sensor.rgb()
    currentColor = " "
    bestDistance = 0.0
    for i in range(0, 3):
        #print(AvalibleColors[list(AvalibleColors.keys())[0]][0])
        r = AvalibleColors[list(AvalibleColors.keys())[i]][0] - currentRGB[0]
        g = AvalibleColors[list(AvalibleColors.keys())[i]][1] - currentRGB[1]
        b = AvalibleColors[list(AvalibleColors.keys())[i]][2] - currentRGB[2]
        distance = math.sqrt(abs((r)^2 + (g)^2 + (b)^2))
        if distance < maxdistance and distance < bestDistance or bestDistance == 0: # Giving the color detection some room
            currentColor = list(AvalibleColors.keys())[i]
            bestDistance = distance
        else:
            pass
    return currentColor