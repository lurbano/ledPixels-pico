import board
from ledPixelsPico import *

ledPix = ledPixels(6, board.GP0)

#ledPix.light(4, (0, 100, 0))
ledPix.rainbowForever()
print("hi")
