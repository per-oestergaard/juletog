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

print("testhat")

hat = Hat()
print(hat.get())


def log_volt():
    print("{:>4}V".format(hat.get_vin()),end=" ")


log_volt()
print()
# hat.green_led(True)
print("HAT OK")