import board
from ledPixelsPico import *

ledPix = ledPixels(20, board.GP0)

#ledPix.light(4, (0, 100, 0))
ledPix.brightness = 0.1
ledPix.rainbowForever(speed=0.05)
print("hi")
