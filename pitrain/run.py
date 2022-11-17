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
motor_b = PassiveMotor("B")
#color = ColorDistanceSensor('B')


power_a=-10
power_b=-10

def power_down_a():
    power_a=power_a-10
    print("power_a=",power_a)

def power_up_a():
    power_a=power_a-15
    print("power_a=",power_a)

def power_down_b():
    power_b=power_b-10
    print("power_b=",power_b)

def power_up_b():
    power_b=power_b-15
    print("power_b=",power_b)


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
    print("power_a=",power_a)
    print("power_b=",power_b)
    motor_a.start(power_a)
    motor_b.start(power_b)

def stop():
    motor_a.stop()
    motor_b.stop()

def play():
    try:
        mp3=os.path.join(here,"Free_Test_Data_100KB_MP3.mp3")
        print(mp3)
        print("spawnlp=",os.spawnlp(os.P_NOWAIT, "/usr/bin/mpg321", "/usr/bin/mpg321","-g","25",mp3))
        # playsound(mp3)
    except Exception:
        print("mp3 play did not work")

def play_intro():
    try:
        mp3=os.path.join(here,"sounds","ALRMBell_Bell of a level crossing (ID 0899)_BSB.mp3")
        print(mp3)
        print("spawnlp=",os.spawnlp(os.P_NOWAIT, "/usr/bin/mpg321", "/usr/bin/mpg321","-g","25",mp3))
        # playsound(mp3)
    except Exception:
        print("mp3 play did not work")


def play_shutdown():
    try:
        mp3=os.path.join(here,"sounds","FARTDsgn_Flatulence 1 (ID 0111)_BSB.mp3")
        print(mp3)
        print("spawnlp=",os.spawnlp(os.P_NOWAIT, "/usr/bin/mpg321", "/usr/bin/mpg321","-g","25",mp3))
        # playsound(mp3)
    except Exception:
        print("mp3 play did not work")

def exit():
    stop()
    print("byebye")
    os._exit(1)

def shutdown_now():
    stop()
    print("shutdown now")
    play_shutdown()
    os.system('sudo shutdown now')

keyboard.add_hotkey('s',start)
keyboard.add_hotkey('ctrl+shift+s',start)
keyboard.add_hotkey('t',stop)
keyboard.add_hotkey('p',play)
keyboard.add_hotkey('x', exit)
keyboard.add_hotkey('q',power_up_a)
keyboard.add_hotkey('w',power_down_a)
keyboard.add_hotkey('e',power_up_b)
keyboard.add_hotkey('r',power_down_b)
# keyboard.wait
stop()
play_intro()

ctrlc_count=0

while True:
    try:
        # print("motor=",motor_a.get())
    #    logcolor()
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
