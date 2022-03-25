# ledPixelsPico: Setting up neopixels (WS281x addressable LEDs) on the Raspberry Pi Pico.

Adapting the ledPixels module from [rpi-led-strip](https://github.com/lurbano/rpi-led-strip), to use [circuitpython](https://learn.adafruit.com/getting-started-with-raspberry-pi-pico-circuitpython/neopixel-leds) on the Pico

## Setup:

Hardware:
* Raspberry Pi Pico
* Individually addressable LED strip ([for example](https://www.aliexpress.com/item/4000744445376.html) ) (20 pixels is the default)
* Attach the LED strip to (defaults):
** Data --> GP0
** Power --> VBUS
** Ground --> GND

Environment Setup:
* Connect Pico to computer using USB cable. It should show up as a USB hard drive on your computer named something like RPI-RP2 (you may need to press the BOOTSEL button as you plug it in).
* Copy the adafruit circuitpython file (.uf2) to the RPI-RP2. It should restart and then show up as CIRCUITPY.

Interpreter
* Install an interpreter. I've found it easiest to use [Thonny](https://thonny.org/).
** On Linux I've had to run a [https://forum.micropython.org/viewtopic.php?f=21&t=10028](usermod   command) (and restart) to get Thonny to work well with the Pico:
```
sudo apt install thonny
usermod -a -G dialout $USER
```
* Open Thonny and set the interpreter to `circuitpython`. If the code.py file does not automatically open, you should probably open it.

Running python programs
* On the CIRCUITPY drive, there is a file called `code.py` whatever you place in that file will run. So test the LED strip with the following program, which lights up the first and last lights.
```
import board
import neopixel

pixels = neopixel.NeoPixel(board.GP0, 20)

pixels[0] = (20,0,0)
pixels[-1] = (0,20,0)
```

Learning programming with the Pico and LED strip:
* [Programming Lessons](https://soriki.com/programmingLessons/leds/)



## References:
* Adafruit: neopixels on the Pico: https://learn.adafruit.com/getting-started-with-raspberry-pi-pico-circuitpython/neopixel-leds
* lurbano: [rpi-led-strip repository](https://github.com/lurbano/rpi-led-strip)
