import "main.py"

def follow_path(color_code):
    go_robot_go()
    while ColorSensor.color() == color_code:
        stop()
        drivebase.drive(100,0)
        wait(100)
        stop()
        run_run_right()
        go_robot_go()
        while ColorSensor.color() == 1:
            stop()
