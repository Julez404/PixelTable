#!/usr/bin/python3

from validData import *
from command import *
import sys

# Expected Input
# 1: Which animation
# 2: Color 1
# 3: Color 2
# 4: Text
# 5: Speed

command = ["setAnimation"]
command.append(sys.argv[1])
command.append(sys.argv[2])
command.append(sys.argv[3])
command.append(sys.argv[4])
command.append(sys.argv[5])
setNewCommand(command)

#    f = open("/var/www/pixel/python/.error", "a")
#    f.write(sys.argv[0] + '\n')
#    f.write(sys.argv[1] + '\n')
#    f.close()
