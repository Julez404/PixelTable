#!/usr/bin/python3

from validData import *
import sys

# Expected Input
# 1: Color -> Hex (000000 to FFFFFF)

if (isHex(sys.argv[1]) and strLengthIs(sys.argv[1],6)):
    f = open("/var/www/pixel/python/.exchange", "w+")
    f.write("setAllPixel" + '\n')
    f.write(sys.argv[1] + '\n')
    f.close()
else:
    f = open("/var/www/pixel/python/.error", "a")
    f.write(sys.argv[1:] + '\n')
    f.close()
