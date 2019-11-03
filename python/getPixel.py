#!/usr/bin/python3

from validData import *
from command import *
from readback import *
import sys
import time

# Expected Input
# 1: Row -> 0 to 9
# 2: Column -> 0 to 19

if (
        isInt(sys.argv[1]) and strLengthIs(sys.argv[1],1) and
        isInt(sys.argv[2]) and (strLengthIs(sys.argv[2],1) or strLengthIs(sys.argv[2],2))
    ):
    command = ["PixelToWeb"]
    command.append(sys.argv[1])
    command.append(sys.argv[2])
    setNewCommand(command)

    time.sleep(.3)

    print(readbackGet())
    readbackClear()
else:
    f = open("/var/www/pixel/python/.error", "a")
    f.write(sys.argv[0] + '\n')
    f.write(sys.argv[1] + '\n')
    f.write(sys.argv[2] + '\n')
    f.write(sys.argv[3] + '\n')
    f.close()
