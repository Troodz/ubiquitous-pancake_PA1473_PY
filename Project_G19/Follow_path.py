

def follow_path(drivebase, left_sens):
    if left_sens.reflection() < 20:
        drivebase.drive(-50, 40)
    else:
        drivebase.drive(-50, -40)

def obstical_check(drivebase, ultra_sens, ev3):
    if ultra_sens.distance() < 200:
        drivebase.drive(0, 0)
        ev3.speaker.say("Obstical detected")
