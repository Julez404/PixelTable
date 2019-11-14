#!/usr/bin/python3

from validData import *
from command import *
import time
from readback import *
import sys

# Expected Input

command = ["stopTimer"]
setNewCommand(command)

time.sleep(0.1)

print(readbackGet())
readbackClear()
