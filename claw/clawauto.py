import time
from gpiozero import Button, DigitalOutputDevice
from adafruit_servokit import ServoKit
from adafruit_motorkit import MotorKit # from adafruit_servokit import ServoKit
import clawvariables

#LimitXP = Button(12, pull_up=False)
#LimitXM = Button(13, pull_up=False)
#LimitYP = Button(5, pull_up=False)
#LimitYM = Button(6, pull_up=False)
#LimitZP = Button(19, pull_up=False)
#LimitZM = Button(16, pull_up=False)

#skit.servo[5].set_pulse_width_range(1000, 2000)

from ADCDevice import *

xmotor = clawvariables.mkit.motor3.throttle
ymotor = clawvariables.mkit.motor1.throttle
zmotor = clawvariables.mkit.motor2.throttle

ServoDisable = clawvariables.ServoDisable.on()
ServoEnable = clawvariables.ServoDisable.off()


def setupclawauto():
    if (clawvariables.adc.detectI2C(0x4b)):  # Detect the ads7830
        clawvariables.adc = ADS7830()
        print("ADC FOUND")
        ServoDisable
    else:
        print("No correct I2C address found, \n"
              "Please use command 'i2cdetect -y 1' to check the I2C address! \n"
              "Program Exit. \n");
        exit(-1)

def clawclose():
    ServoEnable
    time.sleep(.1)
    #clawservo.angle = 150 - (clawvariables.adc.analogRead(0)*143/255) # autoclaw close + booster
    clawvariables.skit.servo[5].angle = 43 - (clawvariables.adc.analogRead(4)*15/255)
    print('clawopen 120')
    time.sleep(.1)
    
def clawrelax():
    clawvariables.ServoDisable.on()
    
def clawopen():
    ServoEnable
    time.sleep(.1)
    print('clawopen 120')
    clawvariables.skit.servo[5].angle = 130
    time.sleep(.1)
    ServoDisable

def raiseclaw():
    print('ZP is pressed')
    while clawvariables.LimitZP.is_pressed == 0:
        clawvariables.mkit.motor2.throttle = 1
    print('ZP is pressed')
    clawvariables.mkit.motor2.throttle = 0

def lowerclaw():
    while clawvariables.ClawTension.is_pressed == 1:
        clawvariables.mkit.motor2.throttle = -1
    clawvariables.mkit.motor2.throttle = 0


def sendclaw():
    print('sendclaw start')
    clawvariables.mkit.motor1.throttle = 0
    clawvariables.mkit.motor3.throttle = 0
    clawvariables.ServoDisable.off()
    clawopen()
    time.sleep(.5)
    lowerclaw()
    time.sleep(1)
    #clawsetpoint = adc.analogRead(2)  # read the ADC value of channel 2 **FOR EASY MODE**
    clawclose() #+ (clawsetpoint * .2)
    #        skit.servo[5].angle = clamp(((((200) * 171) / 252)+9), 9, 180)  # calculate the voltage value
    #        print ('Angle : %d'%(skit.servo[5].angle))
    time.sleep(1)
    raiseclaw()
    print('sendclaw end')

def prizechute():
    print('prizechute start')
    while clawvariables.LimitXM.is_pressed == 0 and clawvariables.LimitYM.is_pressed == 0:
        clawvariables.mkit.motor3.throttle = -1
        clawvariables.mkit.motor1.throttle = -1
    clawvariables.mkit.motor3.throttle = 0
    clawvariables.mkit.motor1.throttle = 0
    while clawvariables.LimitXM.is_pressed == 0:
        clawvariables.mkit.motor3.throttle = -1
        print('chute x-')
    clawvariables.mkit.motor3.throttle = 0
    while clawvariables.LimitYM.is_pressed == 0:
        clawvariables.mkit.motor1.throttle = -1
        print('chute y-')
    clawvariables.mkit.motor1.throttle = 0
    clawopen()
    time.sleep(1)
    clawclose()
    print('prizechute end')
    
def returnclaw():
    clawclose()
    clawvariables.ServoDisable.on()
    while clawvariables.LimitXP.is_pressed == 0 and clawvariables.LimitYP.is_pressed == 0:
        clawvariables.mkit.motor3.throttle = 1
        clawvariables.mkit.motor1.throttle = 1
    clawvariables.mkit.motor3.throttle = 0
    clawvariables.mkit.motor1.throttle = 0
    while clawvariables.LimitYP.is_pressed == 0:
        clawvariables.mkit.motor1.throttle = 1
    clawvariables.mkit.motor1.throttle = 0
    while clawvariables.LimitXP.is_pressed == 0:
        clawvariables.mkit.motor3.throttle = 1
    clawvariables.mkit.motor3.throttle = 0
    time.sleep(.5)
    print('returnclaw end')
    return


def destroy():
    clawvariables.mkit.motor1.throttle = 0
    clawvariables.mkit.motor2.throttle = 0
    clawvariables.mkit.motor3.throttle = 0
    clawvariables.ServoDisable


def main():  # Program entrance
    print('Program is starting ... ')
    try:
        print('starting clawauto.py')
        if clawvariables.standardmodeexit == 0:
            setupclawauto()
            sendclaw()
            prizechute()
#            returnclaw()  #too much movement, end at prize chute
            destroy()
        else: 
            print('standardmodeexit == 1')
            destroy()
    except KeyboardInterrupt:  # Press ctrl-c to end the program.
        destroy()
