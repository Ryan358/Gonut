from gpiozero import LED
from signal import pause

white = LED(27)

white.blink()

pause()