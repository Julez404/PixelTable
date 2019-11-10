# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 13:24:28 2019

@author: ipenner
"""
import setPixel
from switchcase import switch

    
def setNumber(offset_x,offset_y,Number,farbe):
    for case in switch(Number):
        
        if case(0):
            setPixel(1+offset_x,3+offset_y,farbe)
            setPixel(2+offset_x,3+offset_y,farbe)
            setPixel(3+offset_x,3+offset_y,farbe)
            setPixel(4+offset_x,3+offset_y,farbe)
            setPixel(5+offset_x,3+offset_y,farbe)
            setPixel(6+offset_x,3+offset_y,farbe)
            setPixel(7+offset_x,3+offset_y,farbe)
            setPixel(8+offset_x,3+offset_y,farbe)
            setPixel(1+offset_x,1+offset_y,farbe)
            setPixel(2+offset_x,1+offset_y,farbe)
            setPixel(3+offset_x,1+offset_y,farbe)
            setPixel(4+offset_x,1+offset_y,farbe)
            setPixel(5+offset_x,1+offset_y,farbe)
            setPixel(6+offset_x,1+offset_y,farbe)
            setPixel(7+offset_x,1+offset_y,farbe)
            setPixel(8+offset_x,1+offset_y,farbe)
            setPixel(1+offset_x,2+offset_y,farbe)
            setPixel(8+offset_x,2+offset_y,farbe)
            break
        
        if case(1):
            setPixel(1+offset_x,3+offset_y,farbe)
            setPixel(2+offset_x,3+offset_y,farbe)
            setPixel(3+offset_x,3+offset_y,farbe)
            setPixel(4+offset_x,3+offset_y,farbe)
            setPixel(5+offset_x,3+offset_y,farbe)
            setPixel(6+offset_x,3+offset_y,farbe)
            setPixel(7+offset_x,3+offset_y,farbe)
            setPixel(8+offset_x,3+offset_y,farbe)
            break
        
        if case(2):
            setPixel(1+offset_x,1+offset_y,farbe)
            setPixel(1+offset_x,2+offset_y,farbe)
            setPixel(1+offset_x,3+offset_y,farbe)
            setPixel(2+offset_x,3+offset_y,farbe)
            setPixel(3+offset_x,3+offset_y,farbe)
            setPixel(4+offset_x,3+offset_y,farbe)
            setPixel(4+offset_x,2+offset_y,farbe)
            setPixel(4+offset_x,1+offset_y,farbe)
            setPixel(5+offset_x,1+offset_y,farbe)
            setPixel(6+offset_x,1+offset_y,farbe)
            setPixel(7+offset_x,1+offset_y,farbe)
            setPixel(8+offset_x,1+offset_y,farbe)
            setPixel(8+offset_x,2+offset_y,farbe)
            setPixel(8+offset_x,3+offset_y,farbe)
            break
        
        if case(3):
            setPixel(1+offset_x,1+offset_y,farbe)
            setPixel(1+offset_x,2+offset_y,farbe)
            setPixel(1+offset_x,3+offset_y,farbe)
            setPixel(2+offset_x,3+offset_y,farbe)
            setPixel(3+offset_x,3+offset_y,farbe)
            setPixel(4+offset_x,3+offset_y,farbe)
            setPixel(5+offset_x,3+offset_y,farbe)
            setPixel(6+offset_x,3+offset_y,farbe)
            setPixel(7+offset_x,3+offset_y,farbe)
            setPixel(8+offset_x,3+offset_y,farbe)
            setPixel(4+offset_x,2+offset_y,farbe)
            setPixel(4+offset_x,1+offset_y,farbe)
            setPixel(8+offset_x,2+offset_y,farbe)
            setPixel(8+offset_x,3+offset_y,farbe)
            break   
        
        if case(4):
            setPixel(1+offset_x,3+offset_y,farbe)
            setPixel(2+offset_x,3+offset_y,farbe)
            setPixel(3+offset_x,3+offset_y,farbe)
            setPixel(4+offset_x,3+offset_y,farbe)
            setPixel(5+offset_x,3+offset_y,farbe)
            setPixel(6+offset_x,3+offset_y,farbe)
            setPixel(7+offset_x,3+offset_y,farbe)
            setPixel(8+offset_x,3+offset_y,farbe)
            setPixel(1+offset_x,1+offset_y,farbe)
            setPixel(2+offset_x,1+offset_y,farbe)
            setPixel(3+offset_x,1+offset_y,farbe)
            setPixel(4+offset_x,1+offset_y,farbe)
            setPixel(4+offset_x,2+offset_y,farbe)
            break
        
        if case(5):
            setPixel(1+offset_x,3+offset_y,farbe)
            setPixel(1+offset_x,2+offset_y,farbe)
            setPixel(1+offset_x,1+offset_y,farbe)
            setPixel(2+offset_x,1+offset_y,farbe)
            setPixel(3+offset_x,1+offset_y,farbe)
            setPixel(4+offset_x,1+offset_y,farbe)
            setPixel(4+offset_x,2+offset_y,farbe)
            setPixel(4+offset_x,3+offset_y,farbe)
            setPixel(5+offset_x,3+offset_y,farbe)
            setPixel(6+offset_x,3+offset_y,farbe)
            setPixel(7+offset_x,3+offset_y,farbe)
            setPixel(8+offset_x,3+offset_y,farbe)
            setPixel(8+offset_x,2+offset_y,farbe)
            setPixel(8+offset_x,1+offset_y,farbe)
            break
        
        if case(6):
            setPixel(1+offset_x,3+offset_y,farbe)
            setPixel(1+offset_x,2+offset_y,farbe)
            setPixel(1+offset_x,1+offset_y,farbe)
            setPixel(2+offset_x,1+offset_y,farbe)
            setPixel(3+offset_x,1+offset_y,farbe)
            setPixel(4+offset_x,1+offset_y,farbe)
            setPixel(5+offset_x,1+offset_y,farbe)
            setPixel(5+offset_x,2+offset_y,farbe)
            setPixel(5+offset_x,3+offset_y,farbe)
            setPixel(6+offset_x,1+offset_y,farbe)
            setPixel(7+offset_x,1+offset_y,farbe)
            setPixel(8+offset_x,1+offset_y,farbe)
            setPixel(8+offset_x,2+offset_y,farbe)
            setPixel(8+offset_x,3+offset_y,farbe)
            setPixel(7+offset_x,3+offset_y,farbe)
            setPixel(6+offset_x,3+offset_y,farbe)
            break
        
        if case(7):
            setPixel(1+offset_x,1+offset_y,farbe)
            setPixel(1+offset_x,2+offset_y,farbe)
            setPixel(1+offset_x,3+offset_y,farbe)
            setPixel(2+offset_x,3+offset_y,farbe)
            setPixel(3+offset_x,3+offset_y,farbe)
            setPixel(4+offset_x,3+offset_y,farbe)
            setPixel(5+offset_x,3+offset_y,farbe)
            setPixel(6+offset_x,3+offset_y,farbe)
            setPixel(7+offset_x,3+offset_y,farbe)
            setPixel(8+offset_x,3+offset_y,farbe)
            break
            
        if case(8):
            setPixel(1+offset_x,3+offset_y,farbe)
            setPixel(1+offset_x,2+offset_y,farbe)
            setPixel(1+offset_x,1+offset_y,farbe)
            setPixel(2+offset_x,1+offset_y,farbe)
            setPixel(3+offset_x,1+offset_y,farbe)
            setPixel(4+offset_x,1+offset_y,farbe)
            setPixel(5+offset_x,1+offset_y,farbe)
            setPixel(4+offset_x,2+offset_y,farbe)
            setPixel(5+offset_x,3+offset_y,farbe)
            setPixel(6+offset_x,1+offset_y,farbe)
            setPixel(7+offset_x,1+offset_y,farbe)
            setPixel(8+offset_x,1+offset_y,farbe)
            setPixel(8+offset_x,2+offset_y,farbe)
            setPixel(8+offset_x,3+offset_y,farbe)
            setPixel(7+offset_x,3+offset_y,farbe)
            setPixel(6+offset_x,3+offset_y,farbe)
            setPixel(2+offset_x,3+offset_y,farbe)
            setPixel(3+offset_x,3+offset_y,farbe)
            setPixel(4+offset_x,3+offset_y,farbe)
            break
        
        if case(9):
            setPixel(1+offset_x,3+offset_y,farbe)
            setPixel(1+offset_x,2+offset_y,farbe)
            setPixel(1+offset_x,1+offset_y,farbe)
            setPixel(2+offset_x,1+offset_y,farbe)
            setPixel(3+offset_x,1+offset_y,farbe)
            setPixel(4+offset_x,1+offset_y,farbe)
            setPixel(4+offset_x,2+offset_y,farbe)
            setPixel(5+offset_x,3+offset_y,farbe)
            setPixel(8+offset_x,1+offset_y,farbe)
            setPixel(8+offset_x,2+offset_y,farbe)
            setPixel(8+offset_x,3+offset_y,farbe)
            setPixel(7+offset_x,3+offset_y,farbe)
            setPixel(6+offset_x,3+offset_y,farbe)
            setPixel(2+offset_x,3+offset_y,farbe)
            setPixel(3+offset_x,3+offset_y,farbe)
            setPixel(4+offset_x,3+offset_y,farbe)
            break
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        