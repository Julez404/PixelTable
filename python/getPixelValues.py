#!/usr/bin/python3

from validData import *
from command import *
import sys
import time

# Expected Input
# None

command = ["getPixelValues"]
setNewCommand(command)

time.sleep(.1)

f = open("/var/www/pixel/python/.readback", "r")
Pixel_Values = f.readline()
f.close()
print(Pixel_Values)
