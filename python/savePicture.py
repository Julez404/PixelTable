#!/usr/bin/python3

from validData import *
import sys

# Expected Input
# 1: Name (isValidPictureName)

    f = open("/var/www/pixel/python/.exchange", "w+")
    if (isValidPictureName(sys.argv[1])):
    f.write("savePicture" + '\n')
    f.write(sys.argv[1] + '\n')
    f.close()
else:
    f = open("/var/www/pixel/python/.error", "a")
    f.write(sys.argv[0] + '\n')
    f.write(sys.argv[1] + '\n')
    f.close()
