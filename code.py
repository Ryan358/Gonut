import time
import digitalio
import board
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode


btn1_pin = board.GP15
btn2_pin = board.GP14
btn3_pin = board.GP13
btn4_pin = board.GP12
btn5_pin = board.GP11

keyboard = Keyboard(usb_hid.devices)

btn1 = digitalio.DigitalInOut(btn1_pin)
btn1.direction = digitalio.Direction.INPUT
btn1.pull = digitalio.Pull.DOWN

btn2 = digitalio.DigitalInOut(btn2_pin)
btn2.direction = digitalio.Direction.INPUT
btn2.pull = digitalio.Pull.DOWN

btn3 = digitalio.DigitalInOut(btn3_pin)
btn3.direction = digitalio.Direction.INPUT
btn3.pull = digitalio.Pull.DOWN

btn4 = digitalio.DigitalInOut(btn4_pin)
btn4.direction = digitalio.Direction.INPUT
btn4.pull = digitalio.Pull.DOWN

btn5 = digitalio.DigitalInOut(btn5_pin)
btn5.direction = digitalio.Direction.INPUT
btn5.pull = digitalio.Pull.DOWN

while True:
    if btn1.value:
        print("button 1 pressed")
        keyboard.press(Keycode.W)
        time.sleep(0.1)
        keyboard.release(Keycode.W)
    if btn2.value:
        print("button 2 pressed")
        keyboard.press(Keycode.D)
        time.sleep(0.1)
        keyboard.release(Keycode.D)
    if btn3.value:
        print("button 3 pressed")
        keyboard.press(Keycode.S)
        time.sleep(0.1)
        keyboard.release(Keycode.S)
    if btn4.value:
        print("button 4 pressed")
        keyboard.press(Keycode.A)
        time.sleep(0.1)
        keyboard.release(Keycode.A)
    if btn5.value:
        print("button 5 pressed")
        keyboard.press(Keycode.Q)
        time.sleep(0.1)
        keyboard.release(Keycode.Q)
    time.sleep(0.1)
