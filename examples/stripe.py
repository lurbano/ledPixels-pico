import board
import neopixel
import time

def changeUp(dt = 0.1):
    for n in range(nPix):
        for i in range(nPix):
            if i <= n:
                pixels[i] = (0,0,20)
            else:
                pixels[i] = (10,10,0)
        time.sleep(dt)

def changeDown(dt = 0.1):
    for n in range(nPix):
        for i in range(nPix):
            if i >= n:
                pixels[nPix-i-1] = (0,0,20)
            else:
                pixels[nPix-i-1] = (10,10,0)
        time.sleep(dt)

def oneAcross(dt=0.1, dp = 1):
    for n in range(nPix):
        for i in range(nPix):
            if i == n:
                pixels[i] = (0,0,20)
            else:
                pixels[i] = (10,10,0)
        time.sleep(dt)


nPix = 20
pixels = neopixel.NeoPixel(board.GP0, nPix)

n = 0
while True:
    oneAcross(0.05)
    time.sleep(0.1)
    oneAcross(0.05, -1)
    pixels[1] = (30,0,0)
    time.sleep(0.1)
    changeUp(.05)
    time.sleep(.1)
    changeDown(.05)
    time.sleep(0.1)
    # n = n+1
    # for i in range(nPix):
    #     if i < n:
    #         pixels[i] = (0,0,20)
    #     else:
    #         pixels[i] = (0,20,0)
    #
    # if n > nPix:
    #     n = 0
    #     time.sleep(0.5)
    # time.sleep(0.1)
