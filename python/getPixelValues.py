#!/usr/bin/python3

from validData import *
from command import *
from readback import *
import sys
import time

# Expected Input
# None

command = ["PixelValuesToWeb"]
setNewCommand(command)

time.sleep(.1)

print(readbackGet())
