# Write your code here :-)
import board
import neopixel
import time

pixels = neopixel.NeoPixel(board.GP0, 20)

for i in range(255):
    pixels[-1] = (i, 0, 0)
    time.sleep(0.01)
