#!/usr/bin/python3

import time
from readback import *
from rpi_ws281x import *
import sys

EOF = ""

def colorWipe(strip, color, wait_ms=50):
    """Wipe color across display a pixel at a time."""
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
        strip.show()
        time.sleep(wait_ms/1000.0)

def theaterChase(strip, color, wait_ms=50, iterations=10):
    """Movie theater light style chaser animation."""
    for j in range(iterations):
        for q in range(3):
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i+q, color)
            strip.show()
            time.sleep(wait_ms/1000.0)
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i+q, 0)

def wheel(pos):
    """Generate rainbow colors across 0-255 positions."""
    if pos < 85:
        return Color(pos * 3, 255 - pos * 3, 0)
    elif pos < 170:
        pos -= 85
        return Color(255 - pos * 3, 0, pos * 3)
    else:
        pos -= 170
        return Color(0, pos * 3, 255 - pos * 3)

def rainbow(strip, wait_ms=20, iterations=1):
    """Draw rainbow that fades across all pixels at once."""
    for j in range(256*iterations):
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, wheel((i+j) & 255))
        strip.show()
        time.sleep(wait_ms/1000.0)

def rainbowCycle(strip, wait_ms=20, iterations=5):
    """Draw rainbow that uniformly distributes itself across all pixels."""
    for j in range(256*iterations):
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, wheel((int(i * 256 / strip.numPixels()) + j) & 255))
        strip.show()
        time.sleep(wait_ms/1000.0)

def theaterChaseRainbow(strip, wait_ms=50):
    """Rainbow movie theater light style chaser animation."""
    for j in range(256):
        for q in range(3):
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i+q, wheel((i+j) % 255))
            strip.show()
            time.sleep(wait_ms/1000.0)
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i+q, 0)

# Start a predefined animation
def setAnimation(parameters):
    state = parameters[0]
    animation = parameters[1]
    while (state == ("setAnimation"+'\n')):
        if (animation == ("rainbow"+'\n')):
            rainbow(strip)
        if (animation == ("theaterChaseRainbow"+'\n')):
            theaterChaseRainbow(strip)
        parameters = getCommand()
        state = parameters[0]
        animation = parameters[1]
    delLastCommand()

def extractNames(data_array):
    size = len(data_array)
    name = ""
    count = 0
    while (count < size):
        if(data_array[count][0] == "n"):
            name += (data_array[count].lstrip("name=")+"~")
        count = count + 1 ;
    return name;


def getAllAnimations(strip,command):
    f = open(".savedAnimations", "r")
    data = []
    last_read = f.readline()
    while(last_read != EOF):
        data.append(last_read.rstrip('\n'))
        last_read = f.readline()
    f.close()
    allAnimations = extractNames(data)
    readbackSet("~"+allAnimations)
