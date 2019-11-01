#!/usr/bin/python3

from rpi_ws281x import *
from pixels import *
from readback import *
import sys

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
            f.close()
            return False
        last_read = f.readline()
        last_read = f.readline()
    f.close()
    return True

def extractNames(data_array):
    size = len(data_array)
    name = ""
    count = 0
    while (count != size):
        name += (data_array[count].lstrip("name=")+"~")
        count = count + 2;
    return name;

def savePicture(led_strip,command):
    # Check if name is already taken
    if (nameIsAvailable(command[1])):
        f = open(".savedPictures", "a")
        f.write("name=" + command[1])
        f.write('\n')
        f.write(getPixelValues(led_strip))
        f.write('\n')
        f.close()

def setPicture(led_strip,command):
    f = open(".savedPictures", "r")
    count = 0
    last_read = f.readline()
    while (last_read != EOF):
        string_check = last_read
        string_check = string_check.lstrip("name=")
        string_check = string_check.rstrip('\n')
        # Check if name is found
        if string_check == command[1]:
            led_values = f.readline()
            readbackSet(led_values)
            setPixelByString(led_values)
            f.close()
            return None
        last_read = f.readline()
        last_read = f.readline()
    f.close()

def getAllPictures(strip,command):
    f = open(".savedPictures", "r")
    data = []
    last_read = f.readline()
    while(last_read != EOF):
        data.append(last_read.rstrip('\n'))
        last_read = f.readline()
    f.close()
    allPictures = extractNames(data)
    readbackSet(allPictures)

def delPicture(command):
    Do_Something = 0
