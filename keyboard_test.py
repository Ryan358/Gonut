import keyboard
from gpiozero import LED

white = LED(27)

while keyboard.is_pressed('space'):
    white.on