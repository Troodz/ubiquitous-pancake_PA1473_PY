
from urllib.parse import urldefrag
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.parameters import Port, Stop, Direction, Button, Color

def pallet_ahead(drivebase, ultra_sens):
    if ultra_sens.distance() < 300:
        return True
    return False
