# Goes with programming lessons on: https://soriki.com/pico/
# Lensyl Urbano

import board
import neopixel
import time
from ledPixelsPico import *

nPix = 60   # 1 pixel per second
brightness = 100

ledPix = ledPixels(nPix, board.GP0)

startTime = time.monotonic()
dt = 0
for i in range(nPix):
    time.sleep(1)
    ledPix.twoColors(i+1, (brightness,0,0), (0,brightness,0))

endTime = time.monotonic()
print(startTime - endTime)
