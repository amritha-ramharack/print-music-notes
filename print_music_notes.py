# +
# Note generator program V4
# Date 26/06/22
# threading cleaned up
# loop still prints a note after breaking

import time
import threading
import random

notes = ['A', 'B', 'C', 'D', 'E', 'F', 'G'] 
octave = ['3', '4', '5'] 
acc = ['flat', 'sharp', 'natural'] 

# set global variable 
musicbreak = True

def musicnotes():
    #global musicbreak
    while musicbreak:
        x = random.choice(notes)
        y = random.choice(octave)
        z = random.choice(acc)
        time.sleep(3)
        print(x + y, z)
        print()


def stop_program():
    global musicbreak
    stopkey=input('Press a letter key to start \nPress Enter to stop \n')
    musicbreak=False
    print('All done')

    
    
n=threading.Thread(target=musicnotes)
i=threading.Thread(target=stop_program)
n.start()
i.start()
