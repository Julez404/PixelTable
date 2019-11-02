#!/usr/bin/python3

from command import *
from readback import *
from validData import *
import time
import sys

# Expected Input
# 1: Name (isValidPictureName)

if (isValidPictureName(sys.argv[1])):
    command = ["setPicture"]
    command.append(sys.argv[1])
    setNewCommand(command)

    time.sleep(.2)
    print(readbackGet())
    readbackClear()

else:
    f = open("/var/www/pixel/python/.error", "a")
    f.write(sys.argv[0] + '\n')
    f.write(sys.argv[1] + '\n')
    f.close()
