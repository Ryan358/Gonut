import time
import digitalio
import board
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

import adafruit_ble
from adafruit_ble.advertising import Advertisement
from adafruit_ble.advertising.standard import ProvideServicesAdvertisement
from adafruit_ble.services.standard.hid import HIDService
from adafruit_ble.services.standard.device_info import DeviceInfoService
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode

btn1_pin = board.D11
btn2_pin = board.D10
btn3_pin = board.D9
btn4_pin = board.D6
btn5_pin = board.D5

hid = HIDService()
keyboard = Keyboard(hid.devices)

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

device_info = DeviceInfoService(software_revision=adafruit_ble.__version__,
                                manufacturer="Adafruit Industries")
advertisement = ProvideServicesAdvertisement(hid)
advertisement.appearance = 961
scan_response = Advertisement()
scan_response.complete_name = "CircuitPython HID"

ble = adafruit_ble.BLERadio()
if not ble.connected:
    print("advertising")
    ble.start_advertising(advertisement, scan_response)
else:
    print("already connected")
    print(ble.connections)


while True:
    while not ble.connected:
        pass
    print("Start typing:")
    
    while ble.connected:
        if btn1.value:
            print("button 1 pressed")
            keyboard.send(Keycode.W)
            time.sleep(0.1)
        if btn2.value:
            print("button 2 pressed")
            keyboard.send(Keycode.D)
            time.sleep(0.1)
        if btn3.value:
            print("button 3 pressed")
            keyboard.send(Keycode.S)
            time.sleep(0.1)
        if btn4.value:
            print("button 4 pressed")
            keyboard.send(Keycode.A)
            time.sleep(0.1)
        if btn5.value:
            print("button 5 pressed")
            keyboard.send(Keycode.Q)
            time.sleep(0.1)
    time.sleep(0.1)
    
ble.start_advertising(advertisement)
