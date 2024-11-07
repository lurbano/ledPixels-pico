#!/bin/bash
cp ../circuitpython/adafruit*9.1.4.uf2 /media/lurbano/RPI-RP2/

sleep 10

GP=${1:-0}
cp -r ../1.examples /media/lurbano/CIRCUITPY/
cp -r ../lib /media/lurbano/CIRCUITPY/
more ../code.py | sed "s/GP.. /GP${GP}/" > /media/lurbano/CIRCUITPY/backup.py
more ../code.py | sed "s/GP.. /GP${GP}/" > /media/lurbano/CIRCUITPY/code.py
