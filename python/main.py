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

strip.setPixelColor(getPixelIndex(int(sys.argv[1]),int(sys.argv[2])),Color(0,255,0))
strip.show()


