import board
from ledPixelsPico import *

ledPix = ledPixels(20, board.GP0)

colors = [(20, 0, 0), (20, 20, 0), (0, 20, 0), (0, 20, 20), (0, 0, 20)]
colors = colors+colors + colors


ledPix.rotateColors(colors)
print("hi")

while True:
    ledPix.rotateColors(colors, startPix=3)
