import time
print('1')
from gpiozero import Button, DigitalOutputDevice
print('2')
from adafruit_motorkit import MotorKit  # from adafruit_servokit import ServoKit
print('3')
from adafruit_servokit import ServoKit
print('4')
from inputs import get_gamepad
print('5')
import clawvariables
print('6')
from threading import Thread
print('7')
from ADCDevice import *
print('8')
skit = ServoKit(channels=16)
mkit = MotorKit()

print('motorxystandard imports done')

def motorcutoffx():
    clawvariables.mkit.motor3.throttle = 0
    print('motorcutoffx')


def motorcutoffy():
    clawvariables.mkit.motor1.throttle = 0
    print('motorcutoffy')

def motorcutoffz():
    clawvariables.mkit.motor2.throttle = 0
    print('motorcutoffx')

def setupxy():
    clawvariables.mkit.motor1.throttle = 0
    clawvariables.mkit.motor3.throttle = 0

def clawclose():
    ServoDisable.off()
    time.sleep(.1)
    clawvariables.skit.servo[5].angle = 20
    time.sleep(.1)

def loopxy():
    clawvariables.ServoDisable.on()
    loopxyexit = 0
#    while get_gamepad('Key','BTN_BASE3',0) and get_gamepad('Key','BTN_BASE',0):
    while loopxyexit == 0:
        #        if LimitXP.is_pressed:
        #            print('gpio works x+')
        events = get_gamepad()
        #        print(f'%d'%int(LimitXP.value))
        for event in events:
            if event.ev_type == 'Absolute' or 'Key':
                if event.code == 'ABS_X' and 5 <= event.state <= 240:
                    #                    print(f'Left joystick x: {event.state}')
                    clawvariables.mkit.motor3.throttle = 0
                elif event.code == 'ABS_X' and event.state < 5 and clawvariables.LimitXP.is_pressed == 0:
                    #                    print(f'Left joystick x: {event.state}')
                    clawvariables.mkit.motor3.throttle = 1
                elif event.code == 'ABS_X' and event.state > 240 and clawvariables.LimitXM.is_pressed == 0:
                    #                    print(f'Left joystick x: {event.state}')
                    clawvariables.mkit.motor3.throttle = -1
                #            elif event.code == 'ABS_Y' and event.state < 5 and valueYM > 250: #added lim switch
                if event.code == 'ABS_Y' and 5 <= event.state <= 240:
                    #                    print(f'Left joystick YOFF: {event.state}')
                    clawvariables.mkit.motor1.throttle = 0
                elif event.code == 'ABS_Y' and event.state < 5 and clawvariables.LimitYM.is_pressed == 0:
                    #                    print(f'Left joystick Y-: {event.state}')
                    clawvariables.mkit.motor1.throttle = -1
                elif event.code == 'ABS_Y' and event.state > 240 and clawvariables.LimitYP.is_pressed == 0:
                    #                    print(f'Left joystick Y+: {event.state}')
                    clawvariables.mkit.motor1.throttle = 1
                elif event.code == 'BTN_BASE3' and event.state == 1:
                    clawvariables.standardmodeexit = 0
                    print(f'{event.code} : {event.state}')
                    loopxyexit = 1
                elif event.code == 'BTN_BASE4' and event.state == 1:
                    print(f'{event.code} : {event.state}')
                    clawvariables.standardmodeexit = 0
                    loopxyexit = 1
                    print('loopxyexit = 1')
                    print('clawvariables.standardmodeexit = 1')
                elif event.code == 'BTN_BASE5' and event.state == 1:
                    print(f'{event.code} : {event.state}')
                    clawvariables.standardmodeexit = 1
                    print('clawvariables.freeplayexit = 1')
                    loopxyexit = 1
                    print('loopxyzexit = 1')
                elif event.code == 'BTN_BASE6' and event.state == 1:
                    print(f'{event.code} : {event.state}')
                    clawvariables.freeplayexit = 1
                    loopxzexit = 1
        clawvariables.LimitXP.when_pressed = motorcutoffx
        clawvariables.LimitXM.when_pressed = motorcutoffx
        clawvariables.LimitYP.when_pressed = motorcutoffy
        clawvariables.LimitYM.when_pressed = motorcutoffy

def loopxyz():
    loopxyzexit = 0
    while loopxyzexit == 0:
        events = get_gamepad()
        for event in events:
            if event.ev_type == 'Absolute' or 'Key':
                if event.code == 'ABS_X' and 5 <= event.state <= 240:
                    #                    print(f'Left joystick x: {event.state}')
                    clawvariables.mkit.motor3.throttle = 0
                elif event.code == 'ABS_X' and event.state < 5 and clawvariables.LimitXP.is_pressed == 0:
                    #                    print(f'Left joystick x: {event.state}')
                    clawvariables.mkit.motor3.throttle = 0.8
                elif event.code == 'ABS_X' and event.state > 240 and clawvariables.LimitXM.is_pressed == 0:
                    #                    print(f'Left joystick x: {event.state}')
                    clawvariables.mkit.motor3.throttle = -0.8
                #            elif event.code == 'ABS_Y' and event.state < 5 and valueYM > 250: #added lim switch
                if event.code == 'ABS_Y' and 5 <= event.state <= 240:
                    #                    print(f'Left joystick YOFF: {event.state}')
                    clawvariables.mkit.motor1.throttle = 0
                elif event.code == 'ABS_Y' and event.state < 5 and clawvariables.LimitYM.is_pressed == 0:
                    #                    print(f'Left joystick Y-: {event.state}')
                    clawvariables.mkit.motor1.throttle = -0.8
                elif event.code == 'ABS_Y' and event.state > 240 and clawvariables.LimitYP.is_pressed == 0:
                    #                    print(f'Left joystick Y+: {event.state}')
                    clawvariables.mkit.motor1.throttle = 0.8
                if event.code == 'BTN_BASE3' and event.state == 1 and clawvariables.mkit.motor2.throttle == 1:
                    #print(f'{event.code} : {event.state}')
                    clawvariables.mkit.motor2.throttle = 0
                if event.code == 'BTN_BASE4' and event.state == 1 and clawvariables.mkit.motor2.throttle == -1:
                    #print(f'{event.code} : {event.state}')
                    clawvariables.mkit.motor2.throttle = 0
                elif event.code == 'BTN_BASE3' and event.state == 0:
                    #print(f'{event.code} : {event.state}')
                    clawvariables.mkit.motor2.throttle = 0
                elif event.code == 'BTN_BASE4' and event.state == 0:
                    #print(f'{event.code} : {event.state}')
                    clawvariables.mkit.motor2.throttle = 0
                elif event.code == 'BTN_BASE3' and event.state == 1 and clawvariables.ClawTension.is_pressed == 1:
                    #print(f'{event.code} : {event.state}')
                    clawvariables.mkit.motor2.throttle = -0.8
                elif event.code == 'BTN_BASE4' and event.state == 1 and clawvariables.LimitZP.is_pressed == 0:
                    #print(f'{event.code} : {event.state}')
                    clawvariables.mkit.motor2.throttle = 0.8
                elif event.code == 'BTN_BASE5' and event.state == 1:
                    print(f'{event.code} : {event.state}')
                    clawvariables.freeplayexit = 1
                    print('clawvariables.freeplayexit = 1')
                    loopxyzexit = 1
                    print('loopxyzexit = 1')
                elif event.code == 'BTN_BASE6' and event.state == 1:
                    print(f'{event.code} : {event.state}')
                    clawvariables.freeplayexit = 1
                    loopxyzexit = 1
        clawvariables.LimitXP.when_pressed = motorcutoffx
        clawvariables.LimitXM.when_pressed = motorcutoffx
        clawvariables.LimitYP.when_pressed = motorcutoffy
        clawvariables.LimitYM.when_pressed = motorcutoffy
        clawvariables.LimitZP.when_pressed = motorcutoffz
        clawvariables.LimitZM.when_pressed = motorcutoffz
        clawvariables.ClawTension.when_released = motorcutoffz


def clawpotsetup():
    clawvariables.adc
    print('clawvariables.adc')
    if(clawvariables.adc.detectI2C(0x4b)): # Detect the ads7830
        clawvariables.adc = ADS7830()
        print("ADC FOUND")
    else:
        print("No correct I2C address found, \n"
        "Please use command 'i2cdetect -y 1' to check the I2C address! \n"
        "Program Exit. \n");
        exit(-1)

def clamp(angle, min, max):
    if angle < min:
        return min
    elif angle > max:
        return max
    else:
        return angle

def clawpotloop():
    time.sleep(.1)
    print('clawpotloop')
    clawvariables.freeplayexit = 0
    clawvariables.ServoDisable.off()
    while clawvariables.freeplayexit == 0:# clawpotall.is_alive() == 1:
        hpotVoltage = clawvariables.adc.analogRead(2)    # read the ADC value of channel 2
        #print (hpotVoltage)
        clawvariables.skit.servo[5].angle = clamp(((((hpotVoltage) * 171) / 255)+30), 30, 155)  # calculate the voltage value
#        kit.servo[5].angle = clamp(((((200) * 171) / 252)+9), 9, 180)  # calculate the voltage value
        #print ('Angle : %d'%(skit.servo[5].angle))
        time.sleep(0.08)
        
def clawpotdestroy():
    clawvariables.adc.close()
        
def clawpotall():
    clawpotsetup()
    clawpotloop()
#def clawpotall():
#    clawpotxyz()
#testing 7/4    clawpotdestroy()
        
def clawpotxyzclaw():
#    Thread(target = loopxyz).start()
#    Thread(target = loopxyz).IsBackground = True
    Thread(target = clawpotall).start()
    Thread(target = clawpotall).IsBackground = True
    loopxyz()

def destroy():
    mkit.motor1.throttle = 0
    mkit.motor2.throttle = 0
    mkit.motor3.throttle = 0
    clawvariables.ServoDisable.on()
#was getting a file object error     clawvariables.adc.close()  #file object errno 9
    
#def destroy():
#    mkit.motor1.throttle = 0
#    mkit.motor2.throttle = 0
#    mkit.motor3.throttle = 0
#    clawvariables.ServoDisable.on()
#    quit(0)

def mainxy():
    print('MotorXY is starting ... ')
    try:
        print('MotorXY is starting ... ')
        setupxy()
        loopxy()
        destroy()
    except KeyboardInterrupt:  # Press ctrl-c to end the program.
        destroy()

def mainxyz():
    print('MotorXY is starting ... ')
    try:
        print('MotorXY is starting ... ')
        setupxy()
        clawpotsetup()
#       loopxy()
        clawpotxyzclaw()
        destroy()
    except KeyboardInterrupt:  # Press ctrl-c to end the program.
        destroy()

if __name__ == '__main__':
    mainxyz()
