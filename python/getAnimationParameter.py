#!/usr/bin/python3

from command import *
from readback import *
from validData import *
import time
import sys

# Expected Input
# 1: Name (isValidAnimationName)

command = ["getAnimationParameter"]
command.append(sys.argv[1])
setNewCommand(command)

time.sleep(.3)

print(readbackGet())
readbackClear()
