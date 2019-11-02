#!/usr/bin/python3

from rpi_ws281x import *
import config
from random import randint
from animations import *
from command import *
from pictures import *
from pixels import *
import sys
import time

#LED_COUNT = 200
#LED_PIN = 18
#LED_FREQ_HZ = 800000
#LED_DMA = 10
#LED_BRIGHTNESS = 255
#LED_INVERT = False
#LED_CHANNEL = 0
#LED_COLUMN_COUNT = 20

led_strip = Adafruit_NeoPixel(config.LED_COUNT, config.LED_PIN, config.LED_FREQ_HZ,config.LED_DMA,config.LED_INVERT,config.LED_BRIGHTNESS,config.LED_CHANNEL)
led_strip.begin()


# Main loop
while True:
    time.sleep(.01)				# Delay Betwee Commands
    command = getCommand()

    if command[0] == ("setPixel"):
        setPixel(led_strip,command)
    if command[0] == ("setAllPixel"):
        setAllPixel(led_strip,command)
    if command[0] == ("setAnimation"):
        setAnimation(led_strip,command)
    if command[0] == ("PixelValuesToWeb"):
        PixelValuesToWeb(led_strip,command)
    if command[0] == ("savePicture"):
        savePicture(led_strip,command)
        delLastCommand()
    if command[0] == ("getAllPictures"):
        getAllPictures(led_strip,command)
        delLastCommand()
    if command[0] == ("setPicture"):
        setPicture(led_strip,command)
        delLastCommand()
    if command[0] == ("delPicture"):
        delPicture(led_strip,command)
        delLastCommand()
    if command[0] == ("getAllAnimations"):
        getAllAnimations(led_strip,command)
        delLastCommand()
