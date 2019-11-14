#!/usr/bin/python3

from validData import *
from command import *
import sys

# Expected Input
# 1: Color Snake
# 2: Color Apple

if (
        isHex(sys.argv[1]) and strLengthIs(sys.argv[1],6) and
        isHex(sys.argv[2]) and strLengthIs(sys.argv[2],6)
    ):
    command = ["startSnake"]
    command.append(sys.argv[1])
    command.append(sys.argv[2])
    setNewCommand(command)
else:
    f = open("/var/www/pixel/python/.error", "a")
    f.write(sys.argv[0] + '\n')
    f.write(sys.argv[1] + '\n')
    f.write(sys.argv[2] + '\n')
    f.close()
