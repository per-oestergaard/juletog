# https://buildhat.readthedocs.io/en/latest/buildhat/index.html#library
# https://github.com/boppreh/keyboard
#
# from pynput.keyboard import Key, Listener
import threading
from buildhat import ColorSensor
from buildhat import ForceSensor, ColorSensor, ColorDistanceSensor
from signal import pause
from buildhat import Motor
from buildhat import PassiveMotor, Hat
import keyboard
import os
import datetime
import sys
# import subprocess
# import pynput.ke
import time
import random
# from playsound import playsound

print("hello world")

hat = Hat(debug=True)
print(hat.get())


def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


def elogtimestamp():
    now = datetime.datetime.now()
    eprint(now.strftime("%H:%M:%S"))


def lognow():
    now = datetime.datetime.now()
    print(now.strftime("%H:%M:%S"), end=" ")


def logln():
    print("", flush=True)


def log(text):
    print(text, end=" ")


def log_volt():
    log("{:>4}V".format(hat.get_vin()))


lognow()
log_volt()
logln()


def is_connected_to_charger():
    return hat.get_vin() > 7.80


def needs_recharge():
    return hat.get_vin() < 7.0


whatif_motor = True
lognow()
if (is_connected_to_charger()):
    log("connected to charger")
else:
    log("not connected to charger")
    whatif_motor = False

logln()

orange_led = False
green_led = False


def led_show():
    global orange_led
    global green_led
    orange_led = random.random()
    green_led = random.random()
    hat.green_led(green_led)
    hat.orange_led(orange_led)


def log_led():
    global orange_led
    global green_led
    if orange_led:
        orange = "O"
    else:
        orange = " "
    if green_led:
        green = "O"
    else:
        green = " "
    log("LED {}{}".format(orange, green))


here = os.path.dirname(__file__)

motor_loco = PassiveMotor("A")
motor_control = PassiveMotor("D")
color = ColorDistanceSensor('C')

power_loco_start = -25
power_control_start = -23
power_loco = power_loco_start
power_control = power_control_start
power_change_increment = 1


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
    log("color")
    log(color.get_color())
    rgb = color.get_color_rgb()
    log("RGB {:>3}.{:>3}.{:>3}".format(rgb[0], rgb[1], rgb[2]))
    log("Segment color={}".format(color.segment_color(rgb[0], rgb[1], rgb[2])))
    log("Dist. {:>3}".format(color.get_distance()))
    log("Reflect {:>3}".format(color.get_reflected_light()))


def start():
    global power_loco
    global power_control
    global whatif_motor
    lognow()
    if whatif_motor:
        log("WHATIF")
    log("power_loco={}".format(power_loco))
    log("power_control={}".format(power_control))
    logln()
    if not whatif_motor:
        motor_loco.start(power_loco)
        motor_control.start(power_control)


def stop():
    global whatif_motor
    if not whatif_motor:
        motor_loco.stop()
        motor_control.stop()


SOUND_bell = "ALRMBell_Bell_of_a_level_crossing_ID_0899_BSB.mp3"
SOUND_dog = "ANMLDog_Old_dog_barking_1_ID_2352_BSB.mp3"
SOUND_canebells = "BELLAnml_Bells_of_santa_claus_2_ID_1124_BSB.mp3"
SOUND_fart = "FARTDsgn_Flatulence_1_ID_0111_BSB.mp3"
SOUND_fartlong = "FARTMisc_Pony_flatulence_2_ID_1855_BSB.mp3"
SOUND_whitexmas = "MUSCToy_White_christmas_music_box_ID_0465_BSB.mp3"
SOUND_hohoho = "VOXMale_Santa_claus_oh_oh_oh_5_ID_2078_BSB.mp3"
SOUND_trainpassing = "TRNTram_Passing_tram_ID_0278_BSB.mp3"
SOUND_trainhorn = "TRNHorn_Whistling_train_2_ID_0226_BSB.mp3"
SOUND_hornshort = "TRNHorn_Whistling_train_1_ID_0225_BSB.mp3"
SOUND_horn1 = "TRNHorn_Train_horn_ID_0277_BSB.mp3"
SOUND_horn2 = "TRNHorn_Train_horn_2_ID_2846_BSB.mp3"
SOUND_steam1 = "TRNHorn_Hiss_of_steam_train_1_ID_0227_BSB.mp3"
SOUND_freetest = "Free_Test_Data_100KB_MP3.mp3"
SOUND_water = "bubbling_water_1.mp3"
SOUND_GlaedeligJul = "GlaedeligJul.mp3"
SOUND_detjuldetcool = "detjuldetcool.mp3"
SOUND_AntonBukser = "AntonBukser.mp3"
SOUND_KomJulSneGaver = "KomJulSneGaver.mp3"
SOUND_no_HAT = "No-HAT.mp3"
SOUND_Sulten_lades = "Sulten_lades.mp3"

idle_sounds = [SOUND_GlaedeligJul, SOUND_AntonBukser, SOUND_detjuldetcool,
               SOUND_canebells, SOUND_dog, SOUND_hohoho, SOUND_fartlong]


def play_sound(sound):
    try:
        mp3 = os.path.join(here, "sounds", sound)
        lognow()
        log(mp3)
        log("spawnlp={}".format(os.spawnlp(os.P_NOWAIT, "/usr/bin/mpg321",
                                           "/usr/bin/mpg321", "-g", "35", mp3)))
        logln()
        # playsound(mp3)
    except Exception:
        lognow()
        log("mp3 play did not work")
        logln()


def play():
    play_sound(SOUND_freetest)


def play_intro():
    play_sound(SOUND_bell)


def play_shutdown():
    play_sound(SOUND_fart)


def exit():
    stop()
    lognow()
    log("byebye")
    logln()
    os._exit(1)


def shutdown_now():
    stop()
    lognow()
    log("shutdown now")
    logln()
    play_shutdown()
    os.system('sudo shutdown now')


def reboot_now():
    stop()
    lognow()
    log("reboot now")
    logln()
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
keyboard.add_hotkey('8', lambda: play_sound(SOUND_canebells))
keyboard.add_hotkey('9', lambda: play_sound(SOUND_GlaedeligJul))
keyboard.add_hotkey('0', lambda: play_sound(SOUND_detjuldetcool))
keyboard.add_hotkey('+', lambda: play_sound(SOUND_AntonBukser))
keyboard.add_hotkey('½', lambda: play_sound(SOUND_KomJulSneGaver))

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
global_counter = 0
last_global_counter = global_counter


def hat_monitor(every_n_seconds=30):
    global global_counter
    global last_global_counter
    threading.Timer(every_n_seconds, hat_monitor).start()
    # put your action here
    if last_global_counter > 0 and global_counter == last_global_counter:
        lognow()
        log("hat_monitor: current={} last={}".format(
            global_counter, last_global_counter))
        logln()
        play_sound(SOUND_no_HAT)
    if needs_recharge():
        play_sound(SOUND_Sulten_lades)
    last_global_counter = global_counter


# to start
hat_monitor()

while True:
    try:
        led_show()
        lognow()
        log("state current={} last={} counter={:>3} gcounter={:>3}".format(
            current_state, last_state, counter, global_counter))
        logcolor()
        log_volt()
        log_led()
        if whatif_motor:
            log("WHATIF")
        log("power loco {:>4} ctl {:>4}".format(power_loco, power_control))
        logln()
        counter += 1
        global_counter += 1
        if global_counter % 15 == 0:
            elogtimestamp()

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
            elif counter == 65:
                play_sound(SOUND_KomJulSneGaver)
            elif counter == 57:
                play_sound(SOUND_whitexmas)
            elif counter == 45 or counter == 48 or counter == 51:
                play_sound(SOUND_trainhorn)
            elif counter == 40:
                play_sound(SOUND_GlaedeligJul)
            elif counter == 30:
                play_sound(SOUND_trainpassing)
            elif counter == 20:
                play_sound(SOUND_detjuldetcool)
            elif counter == 10 or counter == 11 or counter == 12:
                play_sound(SOUND_hornshort)
        elif current_state == STATE_stopping:
            if counter == 4 or counter == 5 or counter == 6 or counter == 7:
                play_sound(SOUND_fart)
            elif counter == 8:
                stop()
                current_state = STATE_stopped
        elif current_state == STATE_stopped:
            # print("stopped", flush=True)
            stop()
            if global_counter % 50 == 0:
                random_idle_sound = random.choice(idle_sounds)
                play_sound(random_idle_sound)
            if global_counter % 290 == 0:
                set_starting_state()
        else:
            lognow()
            log("invalid state: {}".format(current_state))
            logln()
        if current_state != last_state:
            counter = 0
            last_state = current_state

        time.sleep(1)
    except KeyboardInterrupt:
        ctrlc_count = ctrlc_count+1
        if ctrlc_count > 10:
            break
        lognow()
        log("You cannot stop me")
        logln()

lognow()
log("You could stop me anyway")
logln()
stop()
