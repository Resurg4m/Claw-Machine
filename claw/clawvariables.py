from gpiozero import Button, DigitalOutputDevice
from adafruit_servokit import ServoKit
from adafruit_motorkit import MotorKit # from adafruit_servokit import ServoKit
from inputs import get_gamepad
from ADCDevice import *

skit = ServoKit(channels=16)
mkit = MotorKit()

LimitXP = Button(12, pull_up=False)
LimitXM = Button(13, pull_up=False)
LimitYP = Button(5, pull_up=False)
LimitYM = Button(6, pull_up=False)
LimitZP = Button(16, pull_up=False)
LimitZM = Button(19, pull_up=False)
ClawTension = Button(20, pull_up=False)
ServoDisable = DigitalOutputDevice(4)
freeplayexit = 1
standardmodeexit = 1

adc = ADCDevice() # Define an ADCDevice class object
