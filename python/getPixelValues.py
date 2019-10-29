#!/usr/bin/python3

from validData import *
import sys
import time

# Expected Input
# None

f = open("/var/www/pixel/python/.exchange", "w+")
f.write("getPixelValues" + '\n')
f.close()

time.sleep(.1)

f = open("/var/www/pixel/python/.readback", "r")
Pixel_Values = f.readline()
f.close()
print(Pixel_Values)
