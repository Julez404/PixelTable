#!/usr/bin/python3

from command import *
from readback import *
from validData import *
import time
import sys

# Expected Input
# 1: Name (isValidAnimationName)

command = ["getAllAnimations"]
setNewCommand(command)

time.sleep(.1)

print(readbackGet())
readbackClear()
