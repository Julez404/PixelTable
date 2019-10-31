#!/usr/bin/python3

from validData import *
from command import *
import sys

# Expected Input
# 1: Color -> Hex (000000 to FFFFFF)

if (isHex(sys.argv[1]) and strLengthIs(sys.argv[1],6)):
    command = ["setAllPixel" + '\n']
    command.append(sys.argv[1] + '\n')
    setNewCommand(command)
else:
    f = open("/var/www/pixel/python/.error", "a")
    f.write(sys.argv[0] + '\n')
    f.write(sys.argv[1] + '\n')
    f.close()
