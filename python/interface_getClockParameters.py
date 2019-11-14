# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 14:48:53 2019

@author: ipenner
"""

#get einzelnde Ziffern 
def getNumberOne(zahl):
    ziffer = 0
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

    return ziffer

def getNumberTwo(zahl):
    ziffer = 0
    if zahl == 0:
        ziffer = 0

    elif zahl == 1:
        ziffer = 1
    
    elif zahl == 2:
        ziffer = 2
    
    elif zahl == 3:
        ziffer = 3
    
    elif zahl == 4:
        ziffer = 4
    
    elif zahl == 5:
        ziffer = 5
    
    elif zahl == 6:
        ziffer = 6
    
    elif zahl == 7:
        ziffer = 7
    
    elif zahl == 8:
        ziffer = 8
    
    elif zahl == 9:
        ziffer = 9
        
    return ziffer