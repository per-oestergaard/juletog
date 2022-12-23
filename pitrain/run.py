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
    print("{:>4}V".format(hat.get_vin()),end=" ")


log_volt()
print()
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
motor_control = PassiveMotor("D")
color = ColorDistanceSensor('C')

power_loco_start = -25
power_control_start = -23
power_loco = power_loco_start
power_control = power_control_start
power_change_increment=1


def power_down_loco():
    global power_loco
    power_loco = power_loco-power_change_increment
    print("power_loco=", power_loco)


def power_up_loco():
    global power_loco
    power_loco = power_loco+power_change_increment
    print("power_loco=", power_loco)


def power_down_control():
    global power_control
    power_control = power_control-power_change_increment
    print("power_control=", power_control)


def power_up_control():
    global power_control
    power_control = power_control+power_change_increment
    print("power_control=", power_control)


def power_down_both():
    global power_loco
    global power_control
    power_loco = power_loco-power_change_increment
    power_control = power_control-power_change_increment
    print("power_loco=", power_loco)
    print("power_control=", power_control)
    # start()


def power_up_both():
    global power_loco
    global power_control
    power_loco = power_loco+power_change_increment
    power_control = power_control+power_change_increment
    print("power_loco=", power_loco)
    print("power_control=", power_control)
    # start()


def logcolor():
    print("color",end=" ")
    # print("color get", color.get(),end=" ")
    print(color.get_color(),end=" ")
    rgb = color.get_color_rgb()
    print("RGB {:>3}.{:>3}.{:>3}".format(rgb[0], rgb[1], rgb[2]),end=" ")
    # print("HSV", color.rgb_to_hsv(rgb[0], rgb[1], rgb[2]),end=" ")
    print("Segment color", color.segment_color(rgb[0], rgb[1], rgb[2]),end=" ")
    print("Dist. {:>3}".format(color.get_distance()),end=" ")
    print("Reflect {:>3}".format(color.get_reflected_light()),end=" ")


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


SOUND_bell = "ALRMBell_Bell of a level crossing (ID 0899)_BSB.mp3"
SOUND_dog = "ANMLDog_Old dog barking 1 (ID 2352)_BSB.mp3"
SOUND_canebells = "BELLAnml_Bells of santa claus 2 (ID 1124)_BSB.mp3"
SOUND_fart = "FARTDsgn_Flatulence 1 (ID 0111)_BSB.mp3"
SOUND_fartlong = "FARTMisc_Pony flatulence 2 (ID 1855)_BSB.mp3"
SOUND_whitexmas = "MUSCToy_White christmas music box (ID 0465)_BS.mp3"
SOUND_hohoho = "VOXMale_Santa claus oh oh oh 5 (ID 2078)_BSB.mp3"
SOUND_trainpassing = "TRNTram_Passing tram (ID 0278)_BSB.mp3"
SOUND_trainhorn = "TRNHorn_Whistling train 2 (ID 0226)_BSB.mp3"
SOUND_hornshort = "TRNHorn_Whistling train 1 (ID 0225)_BSB.mp3"
SOUND_horn1 = "TRNHorn_Train horn (ID 0277)_BSB.mp3"
SOUND_horn2 = "TRNHorn_Train horn 2 (ID 2846)_BSB.mp3"
SOUND_steam1 = "TRNHorn_Hiss of steam train 1 (ID 0227)_BSB.mp3"
SOUND_freetest = "Free_Test_Data_100KB_MP3.mp3"
SOUND_water = "bubbling_water_1.mp3"


def play_sound(sound):
    try:
        mp3 = os.path.join(here, "sounds", sound)
        print(mp3)
        print("spawnlp=", os.spawnlp(os.P_NOWAIT, "/usr/bin/mpg321",
              "/usr/bin/mpg321", "-g", "35", mp3))
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
    print("byebye", flush=True)
    os._exit(1)


def shutdown_now():
    stop()
    print("shutdown now", flush=True)
    play_shutdown()
    os.system('sudo shutdown now')


def reboot_now():
    stop()
    print("reboot now", flush=True)
    play_shutdown()
    os.system('sudo reboot')




def set_starting_state():
    global current_state
    current_state = STATE_starting


def set_stopping_state():
    global current_state
    current_state = STATE_stopping


keyboard.add_hotkey('1', lambda: play_sound(SOUND_fart))
keyboard.add_hotkey('2', lambda: play_sound(SOUND_whitexmas))
keyboard.add_hotkey('3', lambda: play_sound(SOUND_hohoho))
keyboard.add_hotkey('4', lambda: play_sound(SOUND_fartlong))
keyboard.add_hotkey('5', lambda: play_sound(SOUND_horn1))
keyboard.add_hotkey('6', lambda: play_sound(SOUND_horn2))
keyboard.add_hotkey('7', lambda: play_sound(SOUND_dog))
keyboard.add_hotkey('8', lambda: play_sound(SOUND_canebells))

keyboard.add_hotkey('ctrl+shift+q', power_up_loco)
keyboard.add_hotkey('ctrl+shift+a', power_down_loco)
keyboard.add_hotkey('ctrl+shift+w', power_up_control)
keyboard.add_hotkey('ctrl+shift+s', power_down_control)
keyboard.add_hotkey('ctrl+shift+e', power_up_both)
keyboard.add_hotkey('ctrl+shift+d', power_down_both)

keyboard.add_hotkey('g', stop)
keyboard.add_hotkey('t', start)
keyboard.add_hotkey('s', set_starting_state)
keyboard.add_hotkey('x', set_stopping_state)

keyboard.add_hotkey('ctrl+shift+x', exit)
keyboard.add_hotkey('ctrl+shift+s', shutdown_now)
keyboard.add_hotkey('ctrl+shift+r', reboot_now)


# keyboard.wait
stop()
play_intro()

ctrlc_count = 0

STATE_stopped = 0
STATE_starting = 1
STATE_running = 2
STATE_stopping = 3

current_state = STATE_stopped
last_state = STATE_stopped
counter = 0

while True:
    try:
        print("state current=", current_state, " last=", last_state, " counter={:>3}".format(counter), flush=True,end=" ")
        # print("motor=",motor_loco.get())
        logcolor()
        log_volt()
        print("power loco {:>4} ctl {:>4}".format(power_loco,power_control), end=" ")
        counter += 1
        if current_state == STATE_starting:
            if counter == 0:
                play_sound(SOUND_steam1)
            elif counter == 1:
                start()
            elif counter == 3:
                play_sound(SOUND_steam1)
            elif counter == 4:
                current_state = STATE_running
        elif current_state == STATE_running:
            if counter == 75:
                current_state = STATE_stopping
            elif counter == 57:
                play_sound(SOUND_whitexmas)
            elif counter == 45 or counter == 48 or counter==51:
                play_sound(SOUND_trainhorn)
            elif counter == 30:
                play_sound(SOUND_trainpassing)
            elif counter == 15 or counter == 16 or counter == 17:
                play_sound(SOUND_hornshort)
        elif current_state == STATE_stopping:
            if counter == 4 or counter == 5 or counter ==6 or counter ==7:
                play_sound(SOUND_fart)
            elif counter == 8:
                stop()
                current_state = STATE_stopped
        elif current_state == STATE_stopped:
            # print("stopped", flush=True)
            stop()
        else:
            print("invalid state: ", current_state)
        if current_state != last_state:
            counter = 0
            last_state = current_state

        print(" ...",flush=True)
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
