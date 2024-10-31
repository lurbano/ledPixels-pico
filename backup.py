# Goes with programming lessons on: https://soriki.com/pico/
# Lensyl Urbano

import board
import neopixel

# Settings
nPix = 20               # number of led's in the strip
ledPin = board.GP15     # Pin on the RPi Pico (most likely GP0, GP15, or GP27)

pixels = neopixel.NeoPixel(ledPin, nPix)

pixels[0] = (20,0,0)
pixels[-1] = (0,20,0)
