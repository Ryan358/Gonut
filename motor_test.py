from adafruit_motorkit import MotorKit
import keyboard
import time

kit = MotorKit()

#while keyboard.is_pressed('space'):


kit.motor1.throttle = 1.0
time.sleep(0.5)
kit.motor1.throttle = 0