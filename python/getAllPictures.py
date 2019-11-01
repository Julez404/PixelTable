#!/usr/bin/python3

from command import *
from validData import *
import sys

# Expected Input
# 1: Name (isValidPictureName)

command = ["getAllPictures"]
setNewCommand(command)

time.sleep(.1)

print(readbackGet())
