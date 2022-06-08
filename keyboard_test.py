#! /usr/bin/env python

"""This is the main code that controls the vehicle. This runs on a cronjob on the Pi on startup."""
from __future__ import print_function

import time
from gpiozero import LED
import keyboard

from back_motor_drivers import back_motors, MAX_SPEED
from front_motor_drivers import front_motors, MAX_SPEED

green = LED(2)
red = LED(26)
blue = LED(4)
throttle = 1
delay = 1

front_right = front_motors.motor1
front_left = front_motors.motor2
back_right = back_motors.motor1
back_left = back_motors.motor2

blue.off()
green.off()
red.off()

front_motors.disable()
back_motors.disable()


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


def coast():
    """This disables the motors instead of braking, so it's not too jolty."""
    front_motors.disable()
    back_motors.disable()


# All of these functions are the same: enable the motors, drive them the right directions for a bit, then they coast.
# The directions are probably wrong since the wiring kept getting messed up, so just test and change directions of each
# motor if necessary.
def forward():
    front_motors.enable()
    back_motors.enable()
    red.off()
    green.on()
    front_right.setSpeed(throttle * MAX_SPEED)
    front_left.setSpeed(throttle * MAX_SPEED)
    back_right.setSpeed(throttle * MAX_SPEED)
    back_left.setSpeed(throttle * MAX_SPEED)
    raiseIfFault()
    print('Motors running')
    time.sleep(delay)
    green.off()
    red.on()
    coast()


def backward():
    front_motors.enable()
    back_motors.enable()
    red.off()
    green.on()
    front_right.setSpeed(-throttle * MAX_SPEED)
    front_left.setSpeed(-throttle * MAX_SPEED)
    back_right.setSpeed(-throttle * MAX_SPEED)
    back_left.setSpeed(-throttle * MAX_SPEED)
    raiseIfFault()
    print('Motors running')
    time.sleep(delay)
    green.off()
    red.on()
    coast()


def left():
    front_motors.enable()
    back_motors.enable()
    red.off()
    green.on()
    front_right.setSpeed(throttle * MAX_SPEED)
    front_left.setSpeed(-throttle * MAX_SPEED)
    back_right.setSpeed(-throttle * MAX_SPEED)
    back_left.setSpeed(throttle * MAX_SPEED)
    raiseIfFault()
    print('Motors running')
    time.sleep(delay)
    green.off()
    red.on()
    coast()


def right():
    front_motors.enable()
    back_motors.enable()
    red.off()
    green.on()
    front_right.setSpeed(-throttle * MAX_SPEED)
    front_left.setSpeed(throttle * MAX_SPEED)
    back_right.setSpeed(throttle * MAX_SPEED)
    back_left.setSpeed(-throttle * MAX_SPEED)
    raiseIfFault()
    print('Motors running')
    time.sleep(delay)
    green.off()
    red.on()
    coast()


def spin():
    front_motors.enable()
    back_motors.enable()
    red.off()
    green.on()
    front_right.setSpeed(-throttle * MAX_SPEED)
    front_left.setSpeed(throttle * MAX_SPEED)
    back_right.setSpeed(-throttle * MAX_SPEED)
    back_left.setSpeed(throttle * MAX_SPEED)
    raiseIfFault()
    print('Motors running')
    time.sleep(delay)
    green.off()
    red.on()
    coast()


blue.blink()
time.sleep(40)
# Don't ask me why this is here. Something to do with the boot sequence of the Pi means
# that if the code starts up the motors too early, they won't run. This 40-second delay is the best I can do without
# altering the Pi boot sequence. Turning off "boot to desktop" will help, but I can't do that without losing the
# ability to edit remotely (which I've disabled anyway by now), so good luck.
blue.off()
while True:
    blue.on()
    # Wait for the next event
    time.sleep(delay)  # This prevents kids from holding down a button and zooming away
    event = keyboard.read_event()
    # This just checks for keyboard input and then drives. Pretty simple
    try:
        if event.event_type == keyboard.KEY_DOWN and event.name == 'w':
            print('forward')
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
        elif event.event_type == keyboard.KEY_DOWN and event.name == 'q':
            print('spin')
            spin()
        elif event.event_type == keyboard.KEY_DOWN and event.name == 'esc':
            print('quit')
            blue.off()
            coast()
            break
        else:
            coast()

    except DriverFault as e:
        print("Driver %s fault!" % e.driver_num)
