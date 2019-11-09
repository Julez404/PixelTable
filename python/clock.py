# import time module
import time
import setPixel


# print current date and time
print(time.strftime("%d.%m.%Y %H:%M:%S"))

hours = time.strftime("%H")
minutes = time.strftime("%M")

print(hours)
print(minutes)

if hours == "12":
    print(minutes)
    
#Berechnen, welche Ziffer in Hours


def setNumberOne():
    setPixel(1,3,"red")
    setPixel(2,3,"red")
    setPixel(3,3,"red")
    setPixel(4,3,"red")
    setPixel(5,3,"red")
    setPixel(6,3,"red")
    setPixel(7,3,"red")
    

    