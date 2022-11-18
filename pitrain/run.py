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


def log_volt():
    print("HAT voltage ", hat.get_vin())


log_volt()
# hat.green_led(True)
# time.sleep(1)
# hat.orange_led(True)
# time.sleep(1)
# hat.green_led(False)
# time.sleep(1)
# hat.orange_led(False)
# time.sleep(1)

here = os.path.dirname(__file__)

motor_loco = PassiveMotor("A")
motor_control = PassiveMotor("B")
#color = ColorDistanceSensor('B')

power_loco_start = -35
power_control_start = -40
power_loco = power_loco_start
power_control = power_control_start


def power_down_loco():
    global power_loco
    power_loco = power_loco-5
    print("power_loco=", power_loco)


def power_up_loco():
    global power_loco
    power_loco = power_loco+5
    print("power_loco=", power_loco)


def power_down_control():
    global power_control
    power_control = power_control-5
    print("power_control=", power_control)


def power_up_control():
    global power_control
    power_control = power_control+5
    print("power_control=", power_control)


def power_down_locob():
    global power_loco
    global power_control
    power_loco = power_loco-5
    power_control = power_control-5
    print("power_loco=", power_loco)
    print("power_control=", power_control)
    start()


def power_up_locob():
    global power_loco
    global power_control
    power_loco = power_loco+5
    power_control = power_control+5
    print("power_loco=", power_loco)
    print("power_control=", power_control)
    start()


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
    global power_loco
    global power_control
    print("power_loco=", power_loco)
    print("power_control=", power_control)
    motor_loco.start(power_loco)
    motor_control.start(power_control)


def stop():
    motor_loco.stop()
    motor_control.stop()


SOUND_bell= "ALRMBell_Bell of a level crossing (ID 0899)_BSB.mp3"
SOUND_dog= "ANMLDog_Old dog barking 1 (ID 2352)_BSB.mp3"
SOUND_canebells= "BELLAnml_Bells of santa claus 2 (ID 1124)_BSB.mp3"
SOUND_fart= "FARTDsgn_Flatulence 1 (ID 0111)_BSB.mp3"
SOUND_fartlong= "FARTMisc_Pony flatulence 2 (ID 1855)_BSB.mp3"
SOUND_whitexmas= "MUSCToy_White christmas music box (ID 0465)_BS.mp3"
SOUND_hohoho= "VOXMale_Santa claus oh oh oh 5 (ID 2078)_BSB.mp3"
SOUND_trainpassing="TRNTram_Passing tram (ID 0278)_BSB.mp3"
SOUND_trainhorn= "TRNHorn_Whistling train 2 (ID 0226)_BSB.mp3"
SOUND_hornshort= "TRNHorn_Whistling train 1 (ID 0225)_BSB.mp3"
SOUND_horn1= "TRNHorn_Train horn (ID 0277)_BSB.mp3"
SOUND_horn2= "TRNHorn_Train horn 2 (ID 2846)_BSB.mp3"
SOUND_steam1= "TRNHorn_Hiss of steam train 1 (ID 0227)_BSB.mp3"
SOUND_freetest="Free_Test_Data_100KB_MP3.mp3"
SOUND_water="bubbling_water_1.mp3"

def play_sound(sound):
    try:
        mp3 = os.path.join(here, "sounds", sound)
        print(mp3)
        print("spawnlp=", os.spawnlp(os.P_NOWAIT, "/usr/bin/mpg321",
              "/usr/bin/mpg321", "-g", "25", mp3))
        # playsound(mp3)
    except Exception:
        print("mp3 play did not work")


def play():
    play_sound(SOUND_freetest)

def play_intro():
    play_sound(SOUND_bell)

def play_shutdown():
    play_sound(SOUND_fart)


def exit():
    stop()
    print("byebye",flush=True)
    os._exit(1)


def shutdown_now():
    stop()
    print("shutdown now",flush=True)
    play_shutdown()
    os.system('sudo shutdown now')


def reboot_now():
    stop()
    print("reboot now",flush=True)
    play_shutdown()
    os.system('sudo reboot')


keyboard.add_hotkey('s', start)
keyboard.add_hotkey('ctrl+shift+s', shutdown_now)
keyboard.add_hotkey('ctrl+shift+r', reboot_now)
keyboard.add_hotkey('t', stop)
keyboard.add_hotkey('p', play)
keyboard.add_hotkey('x', exit)
keyboard.add_hotkey('q', power_up_loco)
keyboard.add_hotkey('w', power_down_loco)
keyboard.add_hotkey('e', power_up_control)
keyboard.add_hotkey('r', power_down_control)
keyboard.add_hotkey('a', power_up_locob)
keyboard.add_hotkey('z', power_down_locob)

# keyboard.wait
stop()
play_intro()

ctrlc_count = 0

STATE_stopped=0
STATE_starting=1
STATE_running=2
STATE_stopping=3

current_state=STATE_stopped
last_state=STATE_stopped
counter=0

while True:
    try:
        print("", flush=True)
        # print("motor=",motor_loco.get())
    #    logcolor()
        log_volt()
        counter+=1
        if current_state == STATE_starting:
            if counter == 0:
                play_sound(SOUND_steam1)
            elif counter == 1:
                start()
                current_state=STATE_running
        elif current_state == STATE_running:
            if counter > 60:
                current_state=STATE_stopped
            elif counter > 45:
                play_sound(SOUND_trainhorn)
            elif counter > 30:
                play_sound(SOUND_canebells)
            elif counter > 15:
                play_sound(SOUND_hornshort)
        elif current_state == STATE_stopping:
            if counter > 5:
                play_sound(SOUND_fart)
                stop()
                current_state=STATE_stopped
        elif current_state == STATE_stopped:
            print("stopped",flush=True)
        else:
            print("invalid state: ",current_state)

        last_state=current_state
        time.sleep(1)
        # c = color.wait_for_new_color()
        # print("Found new color", c)
    except KeyboardInterrupt:
        ctrlc_count = ctrlc_count+1
        if ctrlc_count > 10:
            break
        print("You cannot stop me")

print("You could stop me anyway")
stop()
