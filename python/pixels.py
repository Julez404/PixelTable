#!/usr/bin/python3

import time
from rpi_ws281x import *
from command import *
import sys

# Return the Pixelindex by row and column
def getPixelIndex(row,col):
    return row*LED_COLUMN_COUNT+col

# Return Pixelrow
def getPixelRow(pixelIndex):
    return int(pixelIndex/LED_COLUMN_COUNT)

# Return Pixelcolumn
def getPixelColumn(pixelIndex):
    row = getPixelRow(pixelIndex)
    column = pixelIndex - row*LED_COLUMN_COUNT
    return column

# Set single pixel in specific color
def setPixel(strip,parameters):
    row = parameters[1]
    column = parameters[2]
    color_hex = parameters[3]
    color_r = int( color_hex[0]+color_hex[1],16 )
    color_g = int( color_hex[2]+color_hex[3],16 )
    color_b = int( color_hex[4]+color_hex[5],16 )
    index = getPixelIndex(int(row),int(column))

    strip.setPixelColor(index,Color(color_r,color_g,color_b))
    strip.show()
    delLastCommand()

# Set all Pixel to a specific color
def setAllPixel(strip,parameters):
    color_hex = parameters[1]
    color_r = int( color_hex[0]+color_hex[1],16 )
    color_g = int( color_hex[2]+color_hex[3],16 )
    color_b = int( color_hex[4]+color_hex[5],16 )
    for x in range(0, LED_COUNT):
        strip.setPixelColor(x,Color(color_r,color_g,color_b))
    strip.show()
    delLastCommand()

# Return current state of Pixels as string
def getPixelValues(strip,parameters):
    f = open(".readback","w")
    for i in range (0,LED_COUNT):
        f.write(str(getPixelRow(i))+"_"+str(getPixelColumn(i))+"_"+"%06X" % strip.getPixelColor(i)+"-")
    f.close()
    delLastCommand()
