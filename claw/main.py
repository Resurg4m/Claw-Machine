import time
print('time')
#import motorxyzfree
import motorxystandard
print('motorxystandard')
#import clawpot
#print('clawpot')
import clawauto
print('clawauto')
from inputs import get_gamepad
#import threading
#print('threading')
import clawvariables

# set GPIO parameters
global gameover
gameover = False
print('gameover=false')

#def run_script(script_name):
#    subprocess.run(["python", script_name])

#def freescripts(script_name):
#    subprocess.run(["python", script_name])

#    script1_thread = threading.Thread(target=run_script, args=("motorxystandard.py",))
#    script2_thread = threading.Thread(target=run_script, args=("clawpot.py",))

#    script1_thread.start()
#    script2_thread.start()

#    script1_thread.join()
#    script2_thread.join()
#def double():
#    subprocess.run("python3 script1.py & python3 script2.py", shell=True)
#    print("Both scripts have finished executing.")


def freeplay():
#    subprocess.run("python3 motorxystandard.py & python3 clawpot.py", shell=True)
#    freescripts(motorxyzfree.py & clawpot.py)
    print('freescripts (standard)')
    motorxystandard.mainxyz()
    gameover = True
    return

def standardmode():
    motorxystandard.mainxy()
#    motorxystandard.loopxy()
    clawauto.main()
    gameover = True
    return

def main():
    print('Starting Claw Machine')
    gameover = False
    clawvariables.ServoDisable.on()
    mainscreenprinted = 0
    while not gameover: #Waiting for button press to define gamemode
        if mainscreenprinted == 0:
            print("""
            Main Screen:
            Coin = Standard
            1 Player = Freeplay
            """)
            mainscreenprinted = 1
        events = get_gamepad()
        for event in events:
            if event.ev_type == 'Key' and not gameover:
                if event.code == 'BTN_BASE6' and event.state == 1:
                    print('Starting Free Play')
                    freeplay()
                    print('game over')
                    mainscreenprinted = 0
                elif event.code == 'BTN_BASE5' and event.state == 1:
                    print('Starting Standard Timed Mode')
                    clawvariables.ServoDisable.off()
                    standardmode()
                    print('game over')
                    mainscreenprinted = 0
            break

if __name__ == '__main__':
    main()
