from __future__ import print_function
import time
from front_motor_drivers import front_motors, MAX_SPEED

# Define a custom exception to raise if a fault is detected.
class DriverFault(Exception):
    def __init__(self, driver_num):
        self.driver_num = driver_num

def raiseIfFault():
    if front_motors.motor1.getFault():
        raise DriverFault(1)
    if front_motors.motor2.getFault():
        raise DriverFault(2)

# Set up sequences of motor speeds.
test_forward_speeds = list(range(0, MAX_SPEED, 1)) + \
  [MAX_SPEED] * 200 + list(range(MAX_SPEED, 0, -1)) + [0]  

test_reverse_speeds = list(range(0, -MAX_SPEED, -1)) + \
  [-MAX_SPEED] * 200 + list(range(-MAX_SPEED, 0, 1)) + [0]  

try:
    front_motors.setSpeeds(0, 0)

    print("Motor 1 forward")
    for s in test_forward_speeds:
        front_motors.motor1.setSpeed(s)
        raiseIfFault()
        time.sleep(0.002)

    print("Motor 1 reverse")
    for s in test_reverse_speeds:
        front_motors.motor1.setSpeed(s)
        raiseIfFault()
        time.sleep(0.002)

    # Disable the drivers for half a second.
    front_motors.disable()
    time.sleep(0.5)
    front_motors.enable()

    print("Motor 2 forward")
    for s in test_forward_speeds:
        front_motors.motor2.setSpeed(s)
        raiseIfFault()
        time.sleep(0.002)

    print("Motor 2 reverse")
    for s in test_reverse_speeds:
        front_motors.motor2.setSpeed(s)
        raiseIfFault()
        time.sleep(0.002)

except DriverFault as e:
    print("Driver %s fault!" % e.driver_num)

finally:
  # Stop the motors, even if there is an exception
  # or the user presses Ctrl+C to kill the process.
    front_motors.forceStop()
