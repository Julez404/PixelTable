#!/usr/bin/python3

from rpi_ws281x import *
from random import randint
from animations import *
import sys
import time

LED_COUNT = 200
LED_PIN = 18
LED_FREQ_HZ = 800000
LED_DMA = 10
LED_BRIGHTNESS = 255
LED_INVERT = False
LED_CHANNEL = 0
LED_COLLUMN_COUNT = 20

strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ,LED_DMA,LED_INVERT,LED_BRIGHTNESS,LED_CHANNEL)
strip.begin()

# Return the Pixelindex by row and column
def getPixelIndex(row,col):
    return row*LED_COLLUMN_COUNT+col

# Set single pixel in specific color
def setPixel():
	f = open(".exchange","r")
	f.readline()

	row = f.readline()
	column = f.readline()
	color_hex = f.readline()
	color_r = int( color_hex[0]+color_hex[1],16 )
	color_g = int( color_hex[2]+color_hex[3],16 )
	color_b = int( color_hex[4]+color_hex[5],16 )
	index = getPixelIndex(int(row),int(column))

	strip.setPixelColor(index,Color(color_r,color_g,color_b))
	strip.show()
	f.close()
	f = open(".exchange","w")
	f.close

# Set all Pixel to a specific color
def setAllPixel():
	f = open(".exchange","r")
	f.readline()
	color_hex = f.readline()
	color_r = int( color_hex[0]+color_hex[1],16 )
	color_g = int( color_hex[2]+color_hex[3],16 )
	color_b = int( color_hex[4]+color_hex[5],16 )
	for x in range(0, LED_COUNT):
		strip.setPixelColor(x,Color(color_r,color_g,color_b))
	strip.show()
	f.close()
	f = open(".exchange","w")
	f.close

# Start a predefined animation
def setAnimation():
    f = open(".exchange","r")
    f.readline()
    animation = f.readline()
    f.close()
    while (animation == ("rainbow" + '\n')):
        rainbow(strip)
        f = open(".exchange","r")
        f.readline()
        animation = f.readline()
        f.close()
    f = open(".exchange","w")
    f.close

# Main loop
while True:
	time.sleep(0.1)				# Delay Betwee Commands
	f = open(".exchange","r")
	input = f.readline()
	f.close()

	if input == ("setPixel"+'\n'):
		setPixel()
	if input == ("setAllPixel"+'\n'):
		setAllPixel()
	if input == ("setAnimation"+'\n'):
		setAnimation()
