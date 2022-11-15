# https://buildhat.readthedocs.io/en/latest/buildhat/index.html#library
# https://github.com/boppreh/keyboard
#
# from pynput.keyboard import Key, Listener
from buildhat import ColorSensor
from buildhat import ForceSensor, ColorSensor, ColorDistanceSensor
from signal import pause
from buildhat import Motor
from buildhat import PassiveMotor, Hat
import keyboard
import os
# import subprocess
# import pynput.ke
import time
# from playsound import playsound

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

here = os.path.dirname(__file__)

motor_a = PassiveMotor("A")
motor_c = PassiveMotor("C")
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
    motor_c.start(5)

def stop():
    motor_a.stop()
    motor_c.stop()

def play():
    try:
        mp3=os.path.join(here,"Free_Test_Data_100KB_MP3.mp3")
        print(mp3)
        print("spawnlp=",os.spawnlp(os.P_NOWAIT, "/usr/bin/mpg321", "/usr/bin/mpg321","-g","25",mp3))
        # playsound(mp3)
    except Exception:
        print("mp3 play did not work")

def exit():
    print("byebye")
    stop()
    os._exit(1)

keyboard.add_hotkey('s',start,suppress=True)
keyboard.add_hotkey('t',stop,suppress=True)
keyboard.add_hotkey('p',play,suppress=True)
keyboard.add_hotkey('x', exit, suppress=True)
# keyboard.wait
stop()

ctrlc_count=0

while True:
    try:
        # print("motor=",motor_a.get())
        logcolor()
        time.sleep(1)
        # c = color.wait_for_new_color()
        # print("Found new color", c)
    except KeyboardInterrupt:
        ctrlc_count=ctrlc_count+1
        if ctrlc_count > 10:
            break
        print("You cannot stop me")

print("You could stop me anyway")
stop()