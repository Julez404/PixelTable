#!/usr/bin/python3

from validData import *
import sys

# Expected Input
# 1: Which animation

f = open("/var/www/pixel/python/.exchange", "w+")
f.write("setAnimation" + '\n')
f.write(sys.argv[1] + '\n')
f.close()

#    f = open("/var/www/pixel/python/.error", "a")
#    f.write(sys.argv[0] + '\n')
#    f.write(sys.argv[1] + '\n')
#    f.close()
