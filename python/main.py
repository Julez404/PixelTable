#!/usr/bin/python3

from rpi_ws281x import *
from random import randint
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


for eachArg in sys.argv:
	print (eachArg)

def getPixelIndex(row,col):
    return row*LED_COLLUMN_COUNT+col


while True:
	f = open(".exchange","r")
	input = f.readline()
	f.close()

	if input == ("setPixel"+'\n'):
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
	time.sleep(0.1)


