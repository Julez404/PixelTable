#!/usr/bin/python3

from rpi_ws281x import *
from pixels import *
import sys

# File: .readback

def readbackSet(data):
    f = open(".readback", "w")
    f.write(data)
    f.close()

def readbackClear():
    f = open(".readback", "w")
    f.close()
