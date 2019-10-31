#!/usr/bin/python3

from rpi_ws281x import *
from random import randint
from animations import *
from command import *
import sys
import time

LED_COUNT = 200
LED_PIN = 18
LED_FREQ_HZ = 800000
LED_DMA = 10
LED_BRIGHTNESS = 255
LED_INVERT = False
LED_CHANNEL = 0
LED_COLUMN_COUNT = 20

strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ,LED_DMA,LED_INVERT,LED_BRIGHTNESS,LED_CHANNEL)
strip.begin()

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
def setPixel(parameters):
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
def setAllPixel(parameters):
    color_hex = parameters[1]
    color_r = int( color_hex[0]+color_hex[1],16 )
    color_g = int( color_hex[2]+color_hex[3],16 )
    color_b = int( color_hex[4]+color_hex[5],16 )
    for x in range(0, LED_COUNT):
        strip.setPixelColor(x,Color(color_r,color_g,color_b))
    strip.show()
    delLastCommand()

# Start a predefined animation
def setAnimation(parameters):
    state = parameters[0]
    animation = parameters[1]
    while (state == ("setAnimation")):
        if (animation == ("rainbow")):
            rainbow(strip)
        if (animation == ("theaterChaseRainbow")):
            theaterChaseRainbow(strip)

        parameters = getCommand()
        state = parameters[0]
        animation = parameters[1]
    delLastCommand()

# Return current state of Pixels as string
def getPixelValues(parameters):
    f = open(".readback","w")
    for i in range (0,LED_COUNT):
        f.write(str(getPixelRow(i))+"_"+str(getPixelColumn(i))+"_"+"%06X" % strip.getPixelColor(i)+"-")
    f.close()
    delLastCommand()

# Main loop
while True:
    time.sleep(.01)				# Delay Betwee Commands
    command = getCommand()

    if command[0] == ("setPixel"+'\n'):
        setPixel(command)
    if command[0] == ("setAllPixel"+'\n'):
        setAllPixel(command)
    if command[0] == ("setAnimation"+'\n'):
        setAnimation(command)
    if command[0] == ("getPixelValues"+'\n'):
        getPixelValues(command)
