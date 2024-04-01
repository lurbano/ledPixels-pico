import board
import neopixel
import time

pixels = neopixel.NeoPixel(board.GP0, 20)

for t in range(5):
    for i in range(255):
        pixels[-1] = (i, 0, 0)
        time.sleep(0.01)

    for i in range(255):
        pixels[-1] = (255-i, 0, 0)
        time.sleep(0.01)
