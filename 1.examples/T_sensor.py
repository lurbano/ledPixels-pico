import board
import neopixel
import time

#***********************************
# START: TEMPERATURE SENSOR SETUP
# ref: https://learn.adafruit.com/using-ds18b20-temperature-sensor-with-circuitpython/circuitpython
import adafruit_ds18x20
from adafruit_onewire.bus import OneWireBus
ow_bus = OneWireBus(board.GP16)
# Identify all onewire devices
devices = ow_bus.scan()
for device in devices:
    print("ROM = {} \tFamily = 0x{:02x}".format([hex(i) for i in device.rom], device.family_code))
# get temperature sensor
ds18b20 = adafruit_ds18x20.DS18X20(ow_bus, devices[0])
print(f'T = {ds18b20.temperature}')
# END: TEMPERATURE SENSOR SETUP
#********************************

nPix = 20  # number of pixels
pixels = neopixel.NeoPixel(board.GP0, nPix)
n = 0
while True:
    time.sleep(1)
    n += 1
    #*************************
    # START: READ TEMPERATURE
    T = ds18b20.temperature
    # END: READ TEMPERATURE
    #*************************
    np = int((ds18b20.temperature - 23)*10) #number of pixels
    print(f'T({n}) {np} = {T}')

    for i in range(nPix):
        if (i <= np):
            pixels[i] = (0, 10, 0)
        else:
            pixels[i] = (0,0,0)
