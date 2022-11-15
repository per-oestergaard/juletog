# https://buildhat.readthedocs.io/en/latest/buildhat/index.html#library
#
from pynput.keyboard import Key, Listener
from buildhat import ColorSensor
from buildhat import ForceSensor, ColorSensor, ColorDistanceSensor
from signal import pause
from buildhat import Motor
from buildhat import PassiveMotor, Hat
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
# motor_a.start(10)
# time.sleep(1)k
# motor_a.stop()

# motor_a.run_for_seconds(5)


# button = ForceSensor('C')
# cs = ColorSensor('B')
color = ColorDistanceSensor('B')
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
    raise Exception("byebye")


# keyboard.on_press_key('s', start())
# keyboard.on_press_key('t', stop())
# keyboard.on_press_key('x', exit())


def on_press(key):
    print("key=", key)
    if key.char == "s":
        start()
    elif key.char == "t":
        stop()
    elif key.char == "x":
        exit()
    else:
        print("Key not supported: {}".format(key.char))


def on_release(key):
    print("key released=", key)


with Listener(on_press=on_press,
              on_release=on_release) as listener:
    listener.join()
# Listener(on_press=on_press,
#               on_release=on_release)


try:
    while True:
        # print("motor=",motor_a.get())
        print("color get", color.get())
        print("color", color.get_color())
        rgb = color.get_color_rgb()
        print("RGB", rgb)
        print("HSV", color.rgb_to_hsv(rgb[0], rgb[1], rgb[2]))
        print("Segment color", color.segment_color(rgb[0], rgb[1], rgb[2]))
        print("Distance", color.get_distance())
        print("Reflected", color.get_reflected_light())
        c = color.wait_for_new_color()
        print("Found new color", c)
except KeyboardInterrupt:
    print("You cannot stop me")
finally:
    print("finally")


# def handle_pressed(force):
#     cs.on()
#     print(cs.get_color())


# def handle_released(force):
#     cs.off()


# button.when_pressed = handle_pressed
# button.when_released = handle_released
# pause()
