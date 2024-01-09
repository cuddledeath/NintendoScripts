from __future__ import annotations

import argparse
import time
import serial

from scripts.switch import SERIAL_DEFAULT

def _press(ser: serial.Serial, s: str, *, duration: float = .05) -> None:
    ser.write(s.encode())
    time.sleep(duration)
    ser.write(b'0')
    time.sleep(.15)

# Function to talk to the jester guy in the casino and play the look away game. 
# Need to win 100 times before he'll give you the Star Egg. 
def look(ser: serial.Serial):
    print("Looking...")
    while True:
        _press(ser, 'A')
        time.sleep(.25)
        _press(ser, 'A')
        time.sleep(.25)
        _press(ser, 'A')
        time.sleep(.25)
        _press(ser, 'A')
        time.sleep(.25)
        _press(ser, 'A')
        time.sleep(.25)
        _press(ser, 'a')
        time.sleep(.25)

# Function to start and connect control. Will close menu back to game.
# Ensure screen is on Change Grip/Order 
def start(ser: serial.Serial):
    print("Starting...")
    _press(ser, 'LR')
    time.sleep(1)
    _press(ser, 'A')
    time.sleep(1)
    _press(ser,'B')
    time.sleep(1)
    _press(ser,'H')

# Function to make character defend
# Make sure a different party member (not NMario) is selected
def defend(ser: serial.Serial):
    print("Defending...")
    _press(ser, 'B')
    time.sleep(.25)
    _press(ser, 'A')
    time.sleep(.25)

# Function to make mario select Super Jump and Jump in timed loops. 
# Make sure Mario is selected, and super jump is highlighted in special menu
# The fames may be off for others, I had Peach, and Geno in the party, with 100 special bar and was fighting the skikey and a flying koopa. 
# I was mostly chasing the best timing throughout the 100 jumps as it would stop working at some points. There may be a more precise time that one could use for a single loop and not need to change the time, but this is what worked for me. 
def jump(ser: serial.Serial):
    special(ser)
    print("Jumping!")
    
    time.sleep(.25)
    _press(ser, 'A') # Select Super Jump

    time.sleep(.25)
    _press(ser, 'A') # Select Spikey

    time.sleep(1)
    _press(ser, 'A') # First Jump

    time.sleep(.7)
    _press(ser, 'A') 

    time.sleep(.7)
    _press(ser, 'A')

    time.sleep(.7)
    _press(ser, 'A')

    time.sleep(.7)
    _press(ser, 'A')

    time.sleep(.75)
    _press(ser, 'A')

    time.sleep(.75)
    _press(ser, 'A')

    time.sleep(.75)
    _press(ser, 'A')

    time.sleep(.7)
    _press(ser, 'A')

    time.sleep(.7)
    _press(ser, 'A')

    time.sleep(.7)
    _press(ser, 'A')

    time.sleep(.68)
    _press(ser, 'A') # 12

    time.sleep(.68)
    _press(ser, 'A') # 13

    time.sleep(.68)
    _press(ser, 'A')

    time.sleep(.68)
    _press(ser, 'A') # 15

    time.sleep(.7)
    _press(ser, 'A') # 16
    
    for i in range(0, 13):
        time.sleep(.68) 
        _press(ser, 'A') #17 - 29

    time.sleep(.68) 
    _press(ser, 'A') # 30

    for i in range(0, 5):
        time.sleep(.685)
        _press(ser, 'A') # 
    
    time.sleep(.68)
    _press(ser, 'A') # 39

    for i in range(0, 8): # 40 - 47
        time.sleep(.6825)
        _press(ser, 'A')

    for i in range(0, 14): # 48 - 61
        time.sleep(.683)
        _press(ser, 'A')

    time.sleep(.6825) # 62
    _press(ser, 'A')

    for i in range(0, 16): # 63 - 78
        time.sleep(.683)
        _press(ser, 'A')

    time.sleep(.6825) # 79
    _press(ser, 'A')
