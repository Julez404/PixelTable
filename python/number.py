# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 13:24:28 2019

@author: ipenner
"""
from pixels import *
from switchcase import switch


def setNumber(strip,offset_x,offset_y,Number,farbe]):
    for case in switch(Number):

        if case(0):
            setPixel(strip,[1+offset_x,3+offset_y,farbe])
            setPixel(strip,[2+offset_x,3+offset_y,farbe])
            setPixel(strip,[3+offset_x,3+offset_y,farbe])
            setPixel(strip,[4+offset_x,3+offset_y,farbe])
            setPixel(strip,[5+offset_x,3+offset_y,farbe])
            setPixel(strip,[6+offset_x,3+offset_y,farbe])
            setPixel(strip,[7+offset_x,3+offset_y,farbe])
            setPixel(strip,[8+offset_x,3+offset_y,farbe])
            setPixel(strip,[1+offset_x,1+offset_y,farbe])
            setPixel(strip,[2+offset_x,1+offset_y,farbe])
            setPixel(strip,[3+offset_x,1+offset_y,farbe])
            setPixel(strip,[4+offset_x,1+offset_y,farbe])
            setPixel(strip,[5+offset_x,1+offset_y,farbe])
            setPixel(strip,[6+offset_x,1+offset_y,farbe])
            setPixel(strip,[7+offset_x,1+offset_y,farbe])
            setPixel(strip,[8+offset_x,1+offset_y,farbe])
            setPixel(strip,[1+offset_x,2+offset_y,farbe])
            setPixel(strip,[8+offset_x,2+offset_y,farbe])
            break

        if case(1):
            setPixel(strip,[1+offset_x,3+offset_y,farbe])
            setPixel(strip,[2+offset_x,3+offset_y,farbe])
            setPixel(strip,[3+offset_x,3+offset_y,farbe])
            setPixel(strip,[4+offset_x,3+offset_y,farbe])
            setPixel(strip,[5+offset_x,3+offset_y,farbe])
            setPixel(strip,[6+offset_x,3+offset_y,farbe])
            setPixel(strip,[7+offset_x,3+offset_y,farbe])
            setPixel(strip,[8+offset_x,3+offset_y,farbe])
            break

        if case(2):
            setPixel(strip,[1+offset_x,1+offset_y,farbe])
            setPixel(strip,[1+offset_x,2+offset_y,farbe])
            setPixel(strip,[1+offset_x,3+offset_y,farbe])
            setPixel(strip,[2+offset_x,3+offset_y,farbe])
            setPixel(strip,[3+offset_x,3+offset_y,farbe])
            setPixel(strip,[4+offset_x,3+offset_y,farbe])
            setPixel(strip,[4+offset_x,2+offset_y,farbe])
            setPixel(strip,[4+offset_x,1+offset_y,farbe])
            setPixel(strip,[5+offset_x,1+offset_y,farbe])
            setPixel(strip,[6+offset_x,1+offset_y,farbe])
            setPixel(strip,[7+offset_x,1+offset_y,farbe])
            setPixel(strip,[8+offset_x,1+offset_y,farbe])
            setPixel(strip,[8+offset_x,2+offset_y,farbe])
            setPixel(strip,[8+offset_x,3+offset_y,farbe])
            break

        if case(3):
            setPixel(strip,[1+offset_x,1+offset_y,farbe])
            setPixel(strip,[1+offset_x,2+offset_y,farbe])
            setPixel(strip,[1+offset_x,3+offset_y,farbe])
            setPixel(strip,[2+offset_x,3+offset_y,farbe])
            setPixel(strip,[3+offset_x,3+offset_y,farbe])
            setPixel(strip,[4+offset_x,3+offset_y,farbe])
            setPixel(strip,[5+offset_x,3+offset_y,farbe])
            setPixel(strip,[6+offset_x,3+offset_y,farbe])
            setPixel(strip,[7+offset_x,3+offset_y,farbe])
            setPixel(strip,[8+offset_x,3+offset_y,farbe])
            setPixel(strip,[4+offset_x,2+offset_y,farbe])
            setPixel(strip,[4+offset_x,1+offset_y,farbe])
            setPixel(strip,[8+offset_x,2+offset_y,farbe])
            setPixel(strip,[8+offset_x,3+offset_y,farbe])
            break

        if case(4):
            setPixel(strip,[1+offset_x,3+offset_y,farbe])
            setPixel(strip,[2+offset_x,3+offset_y,farbe])
            setPixel(strip,[3+offset_x,3+offset_y,farbe])
            setPixel(strip,[4+offset_x,3+offset_y,farbe])
            setPixel(strip,[5+offset_x,3+offset_y,farbe])
            setPixel(strip,[6+offset_x,3+offset_y,farbe])
            setPixel(strip,[7+offset_x,3+offset_y,farbe])
            setPixel(strip,[8+offset_x,3+offset_y,farbe])
            setPixel(strip,[1+offset_x,1+offset_y,farbe])
            setPixel(strip,[2+offset_x,1+offset_y,farbe])
            setPixel(strip,[3+offset_x,1+offset_y,farbe])
            setPixel(strip,[4+offset_x,1+offset_y,farbe])
            setPixel(strip,[4+offset_x,2+offset_y,farbe])
            break

        if case(5):
            setPixel(strip,[1+offset_x,3+offset_y,farbe])
            setPixel(strip,[1+offset_x,2+offset_y,farbe])
            setPixel(strip,[1+offset_x,1+offset_y,farbe])
            setPixel(strip,[2+offset_x,1+offset_y,farbe])
            setPixel(strip,[3+offset_x,1+offset_y,farbe])
            setPixel(strip,[4+offset_x,1+offset_y,farbe])
            setPixel(strip,[4+offset_x,2+offset_y,farbe])
            setPixel(strip,[4+offset_x,3+offset_y,farbe])
            setPixel(strip,[5+offset_x,3+offset_y,farbe])
            setPixel(strip,[6+offset_x,3+offset_y,farbe])
            setPixel(strip,[7+offset_x,3+offset_y,farbe])
            setPixel(strip,[8+offset_x,3+offset_y,farbe])
            setPixel(strip,[8+offset_x,2+offset_y,farbe])
            setPixel(strip,[8+offset_x,1+offset_y,farbe])
            break

        if case(6):
            setPixel(strip,[1+offset_x,3+offset_y,farbe])
            setPixel(strip,[1+offset_x,2+offset_y,farbe])
            setPixel(strip,[1+offset_x,1+offset_y,farbe])
            setPixel(strip,[2+offset_x,1+offset_y,farbe])
            setPixel(strip,[3+offset_x,1+offset_y,farbe])
            setPixel(strip,[4+offset_x,1+offset_y,farbe])
            setPixel(strip,[5+offset_x,1+offset_y,farbe])
            setPixel(strip,[5+offset_x,2+offset_y,farbe])
            setPixel(strip,[5+offset_x,3+offset_y,farbe])
            setPixel(strip,[6+offset_x,1+offset_y,farbe])
            setPixel(strip,[7+offset_x,1+offset_y,farbe])
            setPixel(strip,[8+offset_x,1+offset_y,farbe])
            setPixel(strip,[8+offset_x,2+offset_y,farbe])
            setPixel(strip,[8+offset_x,3+offset_y,farbe])
            setPixel(strip,[7+offset_x,3+offset_y,farbe])
            setPixel(strip,[6+offset_x,3+offset_y,farbe])
            break

        if case(7):
            setPixel(strip,[1+offset_x,1+offset_y,farbe])
            setPixel(strip,[1+offset_x,2+offset_y,farbe])
            setPixel(strip,[1+offset_x,3+offset_y,farbe])
            setPixel(strip,[2+offset_x,3+offset_y,farbe])
            setPixel(strip,[3+offset_x,3+offset_y,farbe])
            setPixel(strip,[4+offset_x,3+offset_y,farbe])
            setPixel(strip,[5+offset_x,3+offset_y,farbe])
            setPixel(strip,[6+offset_x,3+offset_y,farbe])
            setPixel(strip,[7+offset_x,3+offset_y,farbe])
            setPixel(strip,[8+offset_x,3+offset_y,farbe])
            break

        if case(8):
            setPixel(strip,[1+offset_x,3+offset_y,farbe])
            setPixel(strip,[1+offset_x,2+offset_y,farbe])
            setPixel(strip,[1+offset_x,1+offset_y,farbe])
            setPixel(strip,[2+offset_x,1+offset_y,farbe])
            setPixel(strip,[3+offset_x,1+offset_y,farbe])
            setPixel(strip,[4+offset_x,1+offset_y,farbe])
            setPixel(strip,[5+offset_x,1+offset_y,farbe])
            setPixel(strip,[4+offset_x,2+offset_y,farbe])
            setPixel(strip,[5+offset_x,3+offset_y,farbe])
            setPixel(strip,[6+offset_x,1+offset_y,farbe])
            setPixel(strip,[7+offset_x,1+offset_y,farbe])
            setPixel(strip,[8+offset_x,1+offset_y,farbe])
            setPixel(strip,[8+offset_x,2+offset_y,farbe])
            setPixel(strip,[8+offset_x,3+offset_y,farbe])
            setPixel(strip,[7+offset_x,3+offset_y,farbe])
            setPixel(strip,[6+offset_x,3+offset_y,farbe])
            setPixel(strip,[2+offset_x,3+offset_y,farbe])
            setPixel(strip,[3+offset_x,3+offset_y,farbe])
            setPixel(strip,[4+offset_x,3+offset_y,farbe])
            break

        if case(9):
            setPixel(strip,[1+offset_x,3+offset_y,farbe])
            setPixel(strip,[1+offset_x,2+offset_y,farbe])
            setPixel(strip,[1+offset_x,1+offset_y,farbe])
            setPixel(strip,[2+offset_x,1+offset_y,farbe])
            setPixel(strip,[3+offset_x,1+offset_y,farbe])
            setPixel(strip,[4+offset_x,1+offset_y,farbe])
            setPixel(strip,[4+offset_x,2+offset_y,farbe])
            setPixel(strip,[5+offset_x,3+offset_y,farbe])
            setPixel(strip,[8+offset_x,1+offset_y,farbe])
            setPixel(strip,[8+offset_x,2+offset_y,farbe])
            setPixel(strip,[8+offset_x,3+offset_y,farbe])
            setPixel(strip,[7+offset_x,3+offset_y,farbe])
            setPixel(strip,[6+offset_x,3+offset_y,farbe])
            setPixel(strip,[2+offset_x,3+offset_y,farbe])
            setPixel(strip,[3+offset_x,3+offset_y,farbe])
            setPixel(strip,[4+offset_x,3+offset_y,farbe])
            break
