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
        name += (data_array[count].lstrip("name=")+"_")
        count = count + 2;
    delLastCommand()
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
    delLastCommand()

def setPicture(led_strip,command):
    f = open(".savedPictures", "r")

    last_read = f.readline()
    while (last_read != EOF):
        string_check = last_read.lstrip("name=")
        string_check = last_read.rstrip('\n')

        # Check if name is found
        if string_check == command[1]:
            readbackSet(f.readline())
            f.close()
            delLastCommand()
            return None
        last_read = f.readline()
        last_read = f.readline()
    f.close()
    delLastCommand()

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
    delLastCommand()

def delPicture(command):
    Do_Something = 0
    delLastCommand()
