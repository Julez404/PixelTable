#!/usr/bin/python3

from validData import *
from command import *
import sys

# Expected Input
# 1: Row -> 0 to 9
# 2: Column -> 0 to 19
# 3: Color -> Hex (000000 to FFFFFF)

if (
        isInt(sys.argv[1]) and strLengthIs(sys.argv[1],1) and
        isInt(sys.argv[2]) and (strLengthIs(sys.argv[2],1) or strLengthIs(sys.argv[2],2)) and
        isHex(sys.argv[3]) and strLengthIs(sys.argv[3],6)
    ):
    command = ["setPixel" + '\n']
    command.append(sys.argv[1] + '\n')
    command.append(sys.argv[2] + '\n')
    command.append(sys.argv[3] + '\n')
    setNewCommand(command)
else:
    f = open("/var/www/pixel/python/.error", "a")
    f.write(sys.argv[0] + '\n')
    f.write(sys.argv[1] + '\n')
    f.write(sys.argv[2] + '\n')
    f.write(sys.argv[3] + '\n')
    f.close()
