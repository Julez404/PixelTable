#!/usr/bin/python3

from validData import *
from command import *
import sys

# Expected Input
# 1: Color -> Hex (000000 to FFFFFF)
# 2: hour
# 3: minute
# 4: second

if (
        isHex(sys.argv[1]) and strLengthIs(sys.argv[1],6)
    ):
    command = ["setTimer"]
    command.append(sys.argv[1])
    command.append(sys.argv[2])
    command.append(sys.argv[3])
    command.append(sys.argv[4])
    setNewCommand(command)
else:
    f = open("/var/www/pixel/python/.error", "a")
    f.write(sys.argv[0] + '\n')
    f.write(sys.argv[1] + '\n')
    f.write(sys.argv[2] + '\n')
    f.write(sys.argv[3] + '\n')
    f.write(sys.argv[4] + '\n')
    f.close()
