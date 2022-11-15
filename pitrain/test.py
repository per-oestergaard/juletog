# https://buildhat.readthedocs.io/en/latest/buildhat/index.html#library
#
# from pynput.keyboard import Key, Listener
from buildhat import ColorSensor
from buildhat import ForceSensor, ColorSensor, ColorDistanceSensor
from signal import pause
from buildhat import Motor
from buildhat import PassiveMotor, Hat
import keyboard
import os
# import pynput.ke
import time
print("hello world")

hat = Hat()
print(hat.get())
print("HAT voltage ", hat.get_vin())
# hat.green_led(True)
# time.sleep(1)
# hat.orange_led(True)
# time.sleep(1)
# hat.green_led(False)
# time.sleep(1)
# hat.orange_led(False)
# time.sleep(1)


motor_a = PassiveMotor("A")
color = ColorDistanceSensor('B')


def logcolor():
    print("color get", color.get())
    print("color", color.get_color())
    rgb = color.get_color_rgb()
    print("RGB", rgb)
    print("HSV", color.rgb_to_hsv(rgb[0], rgb[1], rgb[2]))
    print("Segment color", color.segment_color(rgb[0], rgb[1], rgb[2]))
    print("Distance", color.get_distance())
    print("Reflected", color.get_reflected_light())

def start():
    motor_a.start(5)

def stop():
    motor_a.stop()

def exit():
    print("byebye")
    os._exit(1)

keyboard.add_hotkey('s',start)
keyboard.add_hotkey('t',stop)
keyboard.add_hotkey('x',exit)

while True:
    try:
        # print("motor=",motor_a.get())
        logcolor()
        c = color.wait_for_new_color()
        print("Found new color", c)
    except KeyboardInterrupt:
        print("You cannot stop me")
