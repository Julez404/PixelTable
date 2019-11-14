#!/usr/bin/python3

from validData import *
import sys

# Expected Input
# 1: Message Strin
# 2: Opt: Message color
# 3: Opt: Background color

if(isSupportedByRunningMagazine(sys.argv[1])):
    f = open("/var/www/pixel/python/.exchange", "w+")
    f.write("runningMagazine" + '\n')
    f.write(sys.argv[1] + '\n')
    f.close()
else
    f = open("/var/www/pixel/python/.error", "a")
    f.write(sys.argv[0] + '\n')
    f.write(sys.argv[1] + '\n')
    f.close()
