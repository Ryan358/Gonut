import keyboard
from __future__ import print_function
import time
from front_motor_drivers import front_motors, MAX_SPEED


class DriverFault(Exception):
    def __init__(self, driver_num):
        self.driver_num = driver_num


def raiseIfFault():
    if front_motors.motor1.getFault():
        raise DriverFault(1)
    if front_motors.motor2.getFault():
        raise DriverFault(2)


def forward():
    front_motors.enable()
    front_motors.motor2.setSpeed(MAX_SPEED)
    raiseIfFault()
    print('Motor running')
    time.sleep(0.002)


def coast():
    front_motors.disable()


while True:
    # Wait for the next event.
    event = keyboard.read_event()
    try:
        if event.event_type == keyboard.KEY_DOWN and event.name == 'w':
            print('space was pressed')
            forward()
        else:
            coast()
    except DriverFault as e:
        print("Driver %s fault!" % e.driver_num)
