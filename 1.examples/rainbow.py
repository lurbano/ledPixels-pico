import board
from ledPixelsPico import *

# Pin on the RPi Pico is most likely GP0, GP15, or GP27.
ledPix = ledPixels(20, board.GP0)

#ledPix.light(4, (0, 100, 0))
ledPix.brightness = 0.1
ledPix.rainbowForever(speed=0.05)
print("hi")
