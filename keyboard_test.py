#! /usr/bin/env python
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
    front_motors.disable()
    back_motors.disable()
    
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
time.sleep(2)
blue.off()
while True:
    blue.on()
    # Wait for the next event
    time.sleep(0.5)
    event = keyboard.read_event()
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
