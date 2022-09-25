from m5stack import *
from m5ui import *
from uiflow import *
import unit

neopixel0 = unit.get(unit.NEOPIXEL, unit.PORTA, 29)

# neopixel0.setColorFrom(1, 29, 0x000000) off (black)
# neopixel0.setColorFrom(1, 29, 0xffffff) white
# neopixel0.setColorFrom(1, 29, 0xff0000) red
# neopixel0.setColorFrom(1, 29, 0x33ccff) lightblue
# neopixel0.setColorFrom(1, 29, 0x3366ff) darklue
# neopixel0.setColorFrom(1, 29, 0xff6666) pinkish
# neopixel0.setColorFrom(1, 29, 0xffff00) yellow
# neopixel0.setColorFrom(1, 29, 0x33cc00) green
# neopixel0.setColorFrom(1, 29, 0xcc66cc) purple
color = 1

def buttonA_pressFor():
    # global params
    neopixel0.setBrightness(20)
    pass
btnA.pressFor(0.8, buttonA_pressFor)

def buttonA_wasDoublePress():
    # global params
    neopixel0.setBrightness(3)
    pass
btnA.wasDoublePress(buttonA_wasDoublePress)

def buttonA_wasPressed():
    global color
    if color == 1:
        color = 2
        neopixel0.setColorFrom(1, 29, 0xffffff) # white
        neopixel0.setBrightness(20)
    elif color == 2:
        color = 3
        neopixel0.setColorFrom(1, 29, 0xffffff) # white
        neopixel0.setBrightness(3)
    elif color == 3:
        color = 4
        neopixel0.setColorFrom(1, 29, 0xff0000) # red
        neopixel0.setBrightness(20)
    elif color == 4:
        color = 5
        neopixel0.setColorFrom(1, 29, 0xff0000) # red
        neopixel0.setBrightness(3)
    elif color == 3:
        color = 4
        neopixel0.setColorFrom(1, 29, 0x33ccff) # lightblue
        neopixel0.setBrightness(20)
    elif color == 4:
        color = 5
        neopixel0.setColorFrom(1, 29, 0x33ccff) # lightblue
        neopixel0.setBrightness(3)
    elif color == 5:
        color = 6
        neopixel0.setColorFrom(1, 29, 0x3366ff) # darkblue
        neopixel0.setBrightness(20)
    elif color == 6:
        color = 7
        neopixel0.setColorFrom(1, 29, 0x3366ff) # darkblue
        neopixel0.setBrightness(3)
    elif color == 7:
        color = 8
        neopixel0.setColorFrom(1, 29, 0xff6666) # pinkish
        neopixel0.setBrightness(20)
    elif color == 8:
        color = 9
        neopixel0.setColorFrom(1, 29, 0xff6666) # pinkish
        neopixel0.setBrightness(3)
    elif color == 9:
        color = 10
        neopixel0.setColorFrom(1, 29, 0xffff00) # yellow
        neopixel0.setBrightness(20)
    elif color == 10:
        color = 11
        neopixel0.setColorFrom(1, 29, 0xffff00) # yellow
        neopixel0.setBrightness(3)
    elif color == 11:
        color = 12
        neopixel0.setColorFrom(1, 29, 0x33cc00) # green
        neopixel0.setBrightness(20)
    elif color == 12:
        color = 13
        neopixel0.setColorFrom(1, 29, 0x33cc00) # green
        neopixel0.setBrightness(3)
    elif color == 13:
        color = 14
        neopixel0.setColorFrom(1, 29, 0xcc66cc) # purple
        neopixel0.setBrightness(20)
    elif color == 14:
        color = 15
        neopixel0.setColorFrom(1, 29, 0xcc66cc) # purple
        neopixel0.setBrightness(3)
    elif color == 15:
        color = 1
        neopixel0.setColorFrom(1, 29, 0x000000) #black
        neopixel0.setBrightness(20)
    return

btnA.wasPressed(buttonA_wasPressed)

