#!/usr/bin/python3

import time
import config
from rpi_ws281x import *
from readback import *
from command import *
import sys

# Return the Pixelindex by row and column
def getPixelIndex(row,col):
    return row*config.LED_COLUMN_COUNT+col

# Return Pixelrow
def getPixelRow(pixelIndex):
    return int(pixelIndex/config.LED_COLUMN_COUNT)

# Return Pixelcolumn
def getPixelColumn(pixelIndex):
    row = getPixelRow(pixelIndex)
    column = pixelIndex - row*config.LED_COLUMN_COUNT
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
    for x in range(0, config.LED_COUNT):
        strip.setPixelColor(x,Color(color_r,color_g,color_b))
    strip.show()
    delLastCommand()

# Return current state of Pixels as string
def getPixelValues(strip):
    allPixelValues = ""
    for i in range (0,config.LED_COUNT):
        allPixelValues += (str(getPixelRow(i))+"_"+str(getPixelColumn(i))+"_"+"%06X" % strip.getPixelColor(i)+"-")
    return allPixelValues

# Prints current state of pixel to readback
def PixelValuesToWeb(strip,parameters):
    readbackSet(getPixelValues(strip))
    delLastCommand()


def setPixelByString(strip,data_string):
    string = data_string.rstrip("-")
    string = string.split("-")
    setAllPixel(strip,["","00FF00"])
    count = 0
    for x in string:
        row = getPixelRow(count)
        col = getPixelColumn(count)
        color = x.split("_")
        color = color[2]
        setPixel(strip, ["",row,col,color])
        count = count + 1
