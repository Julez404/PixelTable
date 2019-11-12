# import time module

import time
from number import setNumber
from getClockParameters import getNumberOne
from getClockParameters import getNumberTwo
from pixels import clearPixelBuffer
from command import CommandsAvailable

def clock(strip,parameters):
    while True:
        #löschen
        clearPixelBuffer(strip)

        # print current date and time
        hours = time.strftime("%H")
        minutes = time.strftime("%M")

        #set Doppelpunkt
        Offset_x = 0
        Offset_y = 0
        ziffer = 10
        setNumber(strip, Offset_x, Offset_y, ziffer, parameters[1])

        #set erste Ziffer
        Offset_x = 0
        Offset_y = 0
        zahl = int(hours)
        ziffer = getNumberOne(zahl)
        setNumber(strip, Offset_x, Offset_y, ziffer, parameters[1])

        #set zweite Ziffer
        Offset_x = 0
        Offset_y = 4
        zahl = zahl - (ziffer * 10)
        ziffer = getNumberTwo(zahl)
        setNumber(strip, Offset_x, Offset_y, ziffer, parameters[1])

        #set dritte Ziffer
        Offset_x = 0
        Offset_y = 11
        zahl = int(minutes)
        ziffer = getNumberOne(zahl)
        setNumber(strip, Offset_x, Offset_y, ziffer, parameters[1])
      
        #set vierte Ziffer
        Offset_x = 0
        Offset_y = 15
        zahl = zahl - (ziffer * 10)
        ziffer = getNumberTwo(zahl)
        setNumber(strip, Offset_x, Offset_y, ziffer, parameters[1])
       
        if int(CommandsAvailable()) > 1:
            break




def showTimer(first_number_hours, second_number_hours,
              first_number_minutes, second_number_minutes, 
              first_number_secondes, second_number_secondes,
              strip,parameters):
    

    ziffer_1 = first_number_hours
    ziffer_2 = second_number_hours
    ziffer_3 = first_number_minutes
    ziffer_4 = second_number_minutes
    ziffer_5 = first_number_secondes
    ziffer_6 = second_number_secondes
        
    compare_ziffer_1 = first_number_hours
    compare_ziffer_2 = second_number_hours
    compare_ziffer_3 = first_number_minutes
    compare_ziffer_4 = second_number_minutes
    compare_ziffer_5 = first_number_secondes
    compare_ziffer_6 = second_number_secondes
    
    if((first_number_hours == 0) and (second_number_hours == 0)): 
            setNumber(strip, 0, 0, 10, parameters[1])
            setNumber(strip, 0, 0, ziffer_3, parameters[1])
            setNumber(strip, 0, 4, ziffer_4, parameters[1])
            setNumber(strip, 0, 11, ziffer_5, parameters[1])
            setNumber(strip, 0, 15, ziffer_6, parameters[1])
             
    else: 
            setNumber(strip, 0, 0, 10, parameters[1])
            setNumber(strip, 0, 0, ziffer_1, parameters[1])
            setNumber(strip, 0, 4, ziffer_2, parameters[1])
            setNumber(strip, 0, 11, ziffer_3, parameters[1])
            setNumber(strip, 0, 15, ziffer_4, parameters[1])
    
    
    while True:
        time.sleep(1)
        if(ziffer_6 > 0):
            ziffer_6 = ziffer_6 - 1
            
        elif((ziffer_2 == 0) and (ziffer_1 == 0) and (ziffer_3 == 0) and (ziffer_4 == 0) and (ziffer_5 == 0) and (ziffer_6 == 0)):
            ziffer_6 = 0
            
        elif(ziffer_6 == 0):
            ziffer_6 = 9
            
            if(ziffer_5 > 0):
                ziffer_5 = ziffer_5 - 1
                
            elif((ziffer_2 == 0) and (ziffer_1 == 0) and (ziffer_3 == 0) and (ziffer_4 == 0) and (ziffer_5 == 0)):
                ziffer_5 = 0
                
            elif(ziffer_5 == 0):
                ziffer_5 = 5
                
                if(ziffer_4 > 0):
                    ziffer_4 = ziffer_4 - 1
                    
                elif((ziffer_2 == 0) and (ziffer_1 == 0) and (ziffer_3 == 0) and (ziffer_4 == 0)):
                    ziffer_4 = 0
                    
                elif(ziffer_4 == 0):
                    ziffer_4 = 9
                    
                    if(ziffer_3 > 0):
                        ziffer_3 = ziffer_3 - 1
                        
                    elif((ziffer_2 == 0) and (ziffer_1 == 0) and (ziffer_3 == 0)):
                        ziffer_3 = 0
                        
                    elif(ziffer_3 == 0):
                        ziffer_3 = 5
                        
                        if(ziffer_2 > 0):
                            ziffer_2 = ziffer_2 - 1
                        
                        elif((ziffer_2 == 0) and (ziffer_1 == 0)):
                            ziffer_2 = 0
                            
                        elif(ziffer_2 == 0):
                            ziffer_2 = 9
                            
                            if(ziffer_1 > 0):
                                ziffer_1 = ziffer_1 - 1
                                
                            elif(ziffer_1 == 0):
                                ziffer_1 = 0
        
        
        if((ziffer_1 == 0) and (ziffer_2 == 0)):
           
            setNumber(strip, 0, 0, 10, parameters[1])
            if(compare_ziffer_3 != ziffer_3):
                setNumber(strip, 0, 0, compare_ziffer_3, 000000)
                setNumber(strip, 0, 0, ziffer_3, parameters[1])
                compare_ziffer_3 = ziffer_3 
            if(compare_ziffer_4 != ziffer_4):
                setNumber(strip, 0, 4, compare_ziffer_4, 000000)
                setNumber(strip, 0, 4, ziffer_4, parameters[1])
                compare_ziffer_4 = ziffer_4  
            if(compare_ziffer_5 != ziffer_5):
                setNumber(strip, 0, 11, compare_ziffer_5, 000000)
                setNumber(strip, 0, 11, ziffer_5, parameters[1])
                compare_ziffer_5 = ziffer_5
            if(compare_ziffer_6 != ziffer_6):
                setNumber(strip, 0, 15, compare_ziffer_6, 000000)
                setNumber(strip, 0, 15, ziffer_6, parameters[1])
                compare_ziffer_6 = ziffer_6

             
        else: 
            setNumber(0, 0, 10, parameters[1])
            if(compare_ziffer_1 != ziffer_1):
                setNumber(strip, 0, 0, compare_ziffer_1, 000000)
                setNumber(strip, 0, 0, ziffer_1, parameters[1])
                compare_ziffer_1 = ziffer_1 
            if(compare_ziffer_2 != ziffer_2):
                setNumber(strip, 0, 4, compare_ziffer_2, 000000)
                setNumber(strip, 0, 4, ziffer_2, parameters[1])
                compare_ziffer_2 = ziffer_2
            if(compare_ziffer_3 != ziffer_3):
                setNumber(strip, 0, 11, compare_ziffer_3, 000000)
                setNumber(strip, 0, 11, ziffer_3, parameters[1])
                compare_ziffer_3 = ziffer_3
            if(compare_ziffer_4 != ziffer_4):
                setNumber(strip, 0, 15, compare_ziffer_4, 000000)
                setNumber(strip, 0, 15, ziffer_4, parameters[1])
                compare_ziffer_4 = ziffer_4