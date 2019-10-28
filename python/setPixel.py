#!/usr/bin/python3

import sys


f = open("/var/www/pixel/python/.exchange", "w+")
f.write("setPixel" + '\n')
f.write(sys.argv[1] + '\n')
f.write(sys.argv[2] + '\n')
f.write(sys.argv[3] + '\n')
f.close()
