from adafruit_motorkit import MotorKit
import keyboard
import time

kit = MotorKit()

def forward():
    kit.motor1.throttle =  .30
    kit.motor2.throttle =  .30
    kit.motor3.throttle =  .30
    kit.motor4.throttle =  .30
    
def coast():
    kit.motor1.throttle =  None
    kit.motor2.throttle =  None
    kit.motor3.throttle =  None
    kit.motor4.throttle =  None


while True:
    # Wait for the next event.
    event = keyboard.read_event()
    if event.event_type == keyboard.KEY_DOWN and event.name == 'space':
        print('space was pressed')
        forward()
    else:
        coast()
        
