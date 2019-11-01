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




EOF = ""
# Commands
# [1] Name

# File = .savedPictures

def nameIsAvailable(name):
    f = open(".savedPictures", "r")
    last_read = f.readline()
    while last_read != EOF:
        saved_name = last_read.lstrip("name=")
        saved_name = last_read.rstrip('\n')

        # Name taken -> Return false
        if saved_name == name:
            delLastCommand()
            f.close()
            return False
        last_read = f.readline()
        last_read = f.readline()
    f.close()
    delLastCommand()
    return True

def extractNames(data_array):
    size = len(data_array)
    name = ""
    count = 0
    while (count != size):
        name.append(data_array[count]+"_")
        count = count + 2;
    delLastCommand()
    return name;

def savePicture(led_strip,command):
    # Check if name is already taken
    if (nameIsAvailable(command[1])):
        f = open(".savedPictures", "a")
        f.write("name=" + command[1] + '\n')
        f.write(getPixelValues(led_strip))
        f.close()
    delLastCommand()

def setPicture(command):
    f = open(".savedPictures", "r")

    last_read = f.readline()
    while (last_read != EOF):
        string_check = last_read.lstrip("name=")
        string_check = last_read.rstrip('\n')

        # Check if name is found
        if string_check == command[1]:
            led_values = f.readline()
            readbackSet(led_values)
            f.close()
            break
        last_read = f.readline()
        last_read = f.readline()
    f.close()
    delLastCommand()

def getAllPicturse(command):
    f = open(".savedPictures", "r")
    data = []
    last_read = f.readline()
    while(last_read != EOF):
        data.append(last_read)
        last_read = f.readline()
    f.close()
    allPictures = extractNames(data)
    readbackSet(allPictures)
    delLastCommand()

def delPicture(command):
    Do_Something = 0
    delLastCommand()





# Main loop
while True:
    time.sleep(.01)				# Delay Betwee Commands
    command = getCommand()

    if command[0] == ("setPixel"+'\n'):
        setPixel(led_strip,command)
    if command[0] == ("setAllPixel"+'\n'):
        setAllPixel(led_strip,command)
    if command[0] == ("setAnimation"+'\n'):
        setAnimation(led_strip,command)
    if command[0] == ("PixelValuesToWeb"+'\n'):
        PixelValuesToWeb(led_strip,command)
    if command[0] == ("savePicture"+'\n')
        savePicture(led_strip,command)
