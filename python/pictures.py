import time
from rpi_ws281x import *
import sys
from main import *

# File = .savedPictures

def savePicture(name):
    f = open(".savedPictures", "a")
    f.write("name=" + name + '\n')
    f.write(getPixelValues())
