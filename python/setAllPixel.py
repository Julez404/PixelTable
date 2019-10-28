#!/usr/bin/python3

import sys
import time

for eachArg in sys.argv:
        print (eachArg)

f = open("/var/www/pixel/python/.exchange", "w+")
f.write("setAllPixel" + '\n')
f.write(sys.argv[1] + '\n')
f.close()
