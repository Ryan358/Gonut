from __future__ import print_function

import time

import keyboard

from back_motor_drivers import back_motors, MAX_SPEED
from front_motor_drivers import front_motors, MAX_SPEED

throttle = 0.75


class DriverFault(Exception):
    def __init__(self, driver_num):
        self.driver_num = driver_num


def raiseIfFault():
    if front_motors.motor1.getFault():
        raise DriverFault(1)
    if front_motors.motor2.getFault():
        raise DriverFault(2)
    if back_motors.motor1.getFault():
        raise DriverFault(1)
    if back_motors.motor2.getFault():
        raise DriverFault(2)


def forward():
    front_motors.enable()
    back_motors.enable()
    front_motors.motor1.setSpeed(throttle * MAX_SPEED)
    front_motors.motor2.setSpeed(throttle * MAX_SPEED)
    back_motors.motor1.setSpeed(throttle * MAX_SPEED)
    back_motors.motor2.setSpeed(throttle * MAX_SPEED)
    raiseIfFault()
    print('Motors running')
    time.sleep(0.002)


def backward():
    front_motors.enable()
    back_motors.enable()
    front_motors.motor1.setSpeed(-throttle * MAX_SPEED)
    front_motors.motor2.setSpeed(-throttle * MAX_SPEED)
    back_motors.motor1.setSpeed(-throttle * MAX_SPEED)
    back_motors.motor2.setSpeed(-throttle * MAX_SPEED)
    raiseIfFault()
    print('Motors running')
    time.sleep(0.002)


def right():
    front_motors.enable()
    back_motors.enable()
    front_motors.motor1.setSpeed(throttle * MAX_SPEED)
    front_motors.motor2.setSpeed(-throttle * MAX_SPEED)
    back_motors.motor1.setSpeed(-throttle * MAX_SPEED)
    back_motors.motor2.setSpeed(throttle * MAX_SPEED)
    raiseIfFault()
    print('Motors running')
    time.sleep(0.002)


def left():
    front_motors.enable()
    back_motors.enable()
    front_motors.motor1.setSpeed(-throttle * MAX_SPEED)
    front_motors.motor2.setSpeed(throttle * MAX_SPEED)
    back_motors.motor1.setSpeed(throttle * MAX_SPEED)
    back_motors.motor2.setSpeed(-throttle * MAX_SPEED)
    raiseIfFault()
    print('Motors running')
    time.sleep(0.002)


def coast():
    front_motors.disable()
    back_motors.disable()


while True:
    # Wait for the next event.
    event = keyboard.read_event()
    try:
        if event.event_type == keyboard.KEY_DOWN and event.name == 'w':
            forward()
        elif event.event_type == keyboard.KEY_DOWN and event.name == 'a':
            print('left')
            left()
        elif event.event_type == keyboard.KEY_DOWN and event.name == 's':
            print('backward')
            backward()
        elif event.event_type == keyboard.KEY_DOWN and event.name == 'd':
            print('right')
            right()
        else:
            coast()

    except DriverFault as e:
        print("Driver %s fault!" % e.driver_num)
