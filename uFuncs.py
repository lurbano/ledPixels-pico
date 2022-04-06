import board
import neopixel
import time

nPix = 20
pixels = neopixel.NeoPixel(board.GP0, nPix)

def lightUp(n=nPix, color=(10,0,0), dt=0.1):
    for i in range(n):
        pixels[i] = color
        time.sleep(dt)
