#Bubble Level on Microbit
#Created by: Allison Choi and Yassi Khorsandian

from microbit import *
import math

while True:
    sleep(100)
    x = accelerometer.get_x()
    y = accelerometer.get_y()
    z = accelerometer.get_z()

    rad1 = math.atan2(x, z) #shows the radians in the x-direction
    rad2 = math.atan2(y, z) #shows the radians in the y-direction

    deg1 = (rad1 / math.pi) *180 #shows the degrees in the x-direction
    deg2 = (rad2 / math.pi) *180 #shows the degrees in the y-direction

    print(deg1)
    print(deg2)

    if deg1 >= 170: #if the microbit is level in the x-direction
        if deg2 >= 170:
            display.show(Image.HEART)
        elif deg2 >= 0:
            display.show(Image.ARROW_S)
        else:
            display.show(Image.ARROW_N)
    elif deg2 >= 170: #if the microbit is level in the y-direction
        if deg1 >= 170:
            display.show(Image.HEART)
        elif deg1 > 0:
            display.show(Image.ARROW_E)
        else:
            display.show(Image.ARROW_W)
    elif deg1 < 0:
        if deg2 > 0:
            display.show(Image.ARROW_SW)
        else:
            display.show(Image.ARROW_NW)
    elif deg1 > 0:
        if deg2 > 0:
           display.show(Image.ARROW_SE)
        else:
            display.show(Image.ARROW_NE)
    else:
        blank = Image("00000:"
                      "00000:"
                      "00000:"
                      "00000:"
                      "00000:")
        display.show(blank)

