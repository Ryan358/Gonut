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

while True:
    if btn1.value:
        print("button 1 pressed")
        keyboard.press(Keycode.CONTROL, Keycode.C)
        time.sleep(0.1)
        keyboard.release(Keycode.CONTROL, Keycode.C)
    if btn2.value:
        print("button 2 pressed")
        keyboard.press(Keycode.CONTROL, Keycode.V)
        time.sleep(0.1)
        keyboard.release(Keycode.CONTROL, Keycode.V)
    if btn3.value:
        print("button 3 pressed")
        keyboard.press(Keycode.WINDOWS, Keycode.SHIFT, Keycode.S)
        time.sleep(0.1)
        keyboard.release(Keycode.WINDOWS, Keycode.SHIFT, Keycode.S)
    if btn4.value:
        print("button 4 pressed")
        keyboard.press(Keycode.ALT, Keycode.TAB)
        time.sleep(0.1)
        keyboard.release(Keycode.ALT, Keycode.TAB)
    time.sleep(0.1)