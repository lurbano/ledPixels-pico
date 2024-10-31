#!/bin/bash

# use the gp number as the first command line parameter:
# eg:> transferFiles.sh 0
# the default value is 0

GP=${1:-0}
cp -r ../1.examples /media/lurbano/CIRCUITPY/
cp -r ../lib /media/lurbano/CIRCUITPY/
more ../code.py | sed "s/GP.. /GP${GP}/" > /media/lurbano/CIRCUITPY/backup.py
more ../code.py | sed "s/GP.. /GP${GP}/" > /media/lurbano/CIRCUITPY/code.py
