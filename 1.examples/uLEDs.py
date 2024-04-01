import board
import neopixel
import time

nPix = 20
pixels = neopixel.NeoPixel(board.GP0, nPix)

class uLEDs:
    def __init__(self, nPix=20):
        self.nPix = nPix

    def lightUp(self, n = nPix, color=(10,0,0), dt=0.1):
        for i in range(n):
            pixels[i] = color
            time.sleep(dt)
