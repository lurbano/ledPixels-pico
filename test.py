# Write your code here :-)
import board
import neopixel

pixels = neopixel.NeoPixel(board.D18, 20)

pixels[-3] = (100,0,0)
pixels[-2] = (0,100,0)

