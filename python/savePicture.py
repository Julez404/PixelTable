#!/usr/bin/python3

from validData import *
import sys

# Expected Input
# 1: Name (isValidPictureName)

if (isValidPictureName(sys.argv[1])):
    command = ["savePicture"]
    command.append(sys.argv[1])
    setNewCommand(command)
else:
    f = open("/var/www/pixel/python/.error", "a")
    f.write(sys.argv[0] + '\n')
    f.write(sys.argv[1] + '\n')
    f.close()
