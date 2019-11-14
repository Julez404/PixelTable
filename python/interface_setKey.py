#!/usr/bin/python3

from validData import *
from command import *
import sys

# Expected Input
# 1: Key -> UP,DOWN,RIGHT,LEFT,A,B

if (
        isValidKey(sys.argv[1])
    ):
    command = ["keyPressed"]
    command.append(sys.argv[1])
    setNewCommand(command)
else:
    f = open("/var/www/pixel/python/.error", "a")
    f.write(sys.argv[0] + '\n')
    f.write(sys.argv[1] + '\n')
    f.close()
