import board
from ledPixelsPico import *

ledPix = ledPixels(20, board.GP0)

ledPix.fade(pixFrom=3, pixTo=12, dPix = 2)
print("hi")
