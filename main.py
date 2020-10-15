# Created for a specific task, a bit bodged code, but fully works

# Handle imports
import sounddevice as sd
import numpy as np

from pynput import keyboard
from pynput.keyboard import Key, Controller
import time
import random 

# Settings
duration = 60*60
yesButton = "y"
playButton = "p"
minVol = 50

# Init
keyboard = Controller()
processed = 0
soundPlaying = 0

# Press and release a button
def pressButton(btn):
    keyboard.press(btn)
    keyboard.release(btn)

# Main part of the code
def handleKeys(vol):
    global soundPlaying
    global minVol
    global processed

    if vol > minVol:
        if (soundPlaying == 0):
            print("Recording detected")

        soundPlaying = 150+random.randint(0, 25)
    else:
        if (soundPlaying > 0):
            soundPlaying += -1
            if (soundPlaying == 0):
                processed += 1

                rand = random.randint(0, 100)
                if (rand > 0):
                    pressButton("y")
                    print("Positive")
                else:    
                    pressButton("n")
                    print("Negative")

                print("Total processed " + str(processed) + " recordings")

                time.sleep(1+random.randint(0, 3));

                pressButton("p")
            
def handleSound(indata, outdata, frames, time, status):
    volume_norm = np.linalg.norm(indata)*10
    vol = int(volume_norm)

    # print(("|" * vol) + " " + str(vol))

    handleKeys(vol)

print("Start, awaiting info")

with sd.Stream(callback=handleSound):
    sd.sleep(duration * 1000)

print("End")
