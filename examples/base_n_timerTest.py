import board
import neopixel
from ledPixelsPico import *

nPix = 10

pix = ledPixels(nPix, board.GP0)

n=0
while True:
    pix.base_n_LED(n, base=4, colors=[(0,0,100),(150,50,0),(200,0,0), (0,100,0)])
    n += 1
    time.sleep(1)