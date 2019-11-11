# import time module

import time
from number import setNumber
from pixel import setPixel
from pixel import clearPixelBuffer
from command import CommandsAvailable

def clock(strip,parameters):
    while True:
        #löschen
        clearPixelBuffer(strip)
        
        # print current date and time
        print(time.strftime("%d.%m.%Y %H:%M:%S"))
        
        hours = time.strftime("%H")
        minutes = time.strftime("%M")
        
        print(hours)
        print(minutes)
        
        #set Doppelpunkt
        Offset_x = 0
        Offset_y = 0
        ziffer = 10
        setNumber(Offset_x, Offset_y, ziffer, colour)
        
        #set erste Ziffer
        Offset_x = 0
        Offset_y = 0
        
        zahl = int(hours)
        if(0 <= zahl <= 9):
            ziffer = 0
            
        elif (10 <= zahl <= 19):
            ziffer = 1
            
        elif (20 <= zahl <= 24):
            ziffer = 2
    
        setNumber(strip, Offset_x, Offset_y, ziffer, parameters[1])
        print(ziffer)
        
        
        #set zweite Ziffer
        Offset_x = 0
        Offset_y = 4
        zahl = zahl - (ziffer * 10)
        compare = zahl/2
        
        if compare == 0:
            ziffer = 0
        
        elif compare == 0.5:
            ziffer = 1
            
        elif compare == 1:
            ziffer = 2
            
        elif compare == 1.5:
            ziffer = 3
            
        elif compare == 2:
            ziffer = 4
            
        elif compare == 2.5:
            ziffer = 5
            
        elif compare == 3:
            ziffer = 6
            
        elif compare == 3.5:
            ziffer = 7
            
        elif compare == 4:
            ziffer = 8
            
        elif compare == 4.5:
            ziffer = 9
    
    
        setNumber(strip, Offset_x, Offset_y, ziffer, parameters[1])
        print(ziffer)
        
        #set dritte Ziffer
        Offset_x = 0
        Offset_y = 11
        
        zahl = int(minutes)
        if(0 <= zahl <= 9):
            ziffer = 0
            
        elif (10 <= zahl <= 19):
            ziffer = 1
            
        elif (20 <= zahl <= 29):
            ziffer = 2
            
        elif (30 <= zahl <= 39):
            ziffer = 3
            
        elif (40 <= zahl <= 49):
            ziffer = 4
            
        elif (50 <= zahl <= 59):
            ziffer = 5
        setNumber(strip, Offset_x, Offset_y, ziffer, parameters[1])
        print(ziffer)
        
        #set vierte Ziffer
        Offset_x = 0
        Offset_y = 15
        
        zahl = zahl - (ziffer * 10)
        compare = zahl/2
        if compare == 0:
            ziffer = 0
        
        elif compare == 0.5:
            ziffer = 1
            
        elif compare == 1:
            ziffer = 2
            
        elif compare == 1.5:
            ziffer = 3
            
        elif compare == 2:
            ziffer = 4
            
        elif compare == 2.5:
            ziffer = 5
            
        elif compare == 3:
            ziffer = 6
            
        elif compare == 3.5:
            ziffer = 7
            
        elif compare == 4:
            ziffer = 8
            
        elif compare == 4.5:
            ziffer = 9
        setNumber(strip, Offset_x, Offset_y, ziffer, parameters[1])
        print(ziffer)

        if int(CommandsAvailable()) > 1:
            break
