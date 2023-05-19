import board
import neopixel
from ledPixelsPico import *

nPix = 10

pix = ledPixels(nPix, board.GP0)

# binary time
n=0
for i in range(2**10):
    pix.binaryLED(n)
    n += 1
    time.sleep(1)