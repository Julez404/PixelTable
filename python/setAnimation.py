#!/usr/bin/python3

from validData import *
from command import *
import sys

# Expected Input
# 1: Which animation

command = ["setAnimation" + '\n']
command.append(sys.argv[1] + '\n')
setNewCommand(command)

#    f = open("/var/www/pixel/python/.error", "a")
#    f.write(sys.argv[0] + '\n')
#    f.write(sys.argv[1] + '\n')
#    f.close()
