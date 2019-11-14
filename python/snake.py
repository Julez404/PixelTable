#!/usr/bin/python3

import time
import config
from switchcase import switch
from command import *
from pixels import *
from readback import *
from random import randint

# Constants
NO = 0
YES = 1

# Control
RIGHT = 0
LEFT = 1
UP = 2
DOWN = 3
snake_color = "FFFFFF"
apple_color = "FFFFFF"

# STATE-Machine
STATE = STOPPED
STOPPED = 0
RUNNING = 1
OVER = 2


# Snake Boddy, Start Coordinates
x = [5,6,7]
y = [4,4,4]
x_new = 0
y_new = 0


#
apple = [13,4]

DIRECTION = RIGHT

# Create new Apple on Field
def newApple():
    isTaken = NO

    while True:
        # Calc new Coordinates
        apple = [randint(0,LED_COLUMN_COUNT),randint(0,(LED_COUNT/LED_COLUMN_COUNT))]

        # Check if new Position is on snake
        for i in range(x(len)):
            if ((x[i] == apple[0]) and (y[i] == apple[1])):
                isTaken = YES

        # Repeate or Breakout
        if isTaken == NO:
            break
        else:
            isTaken = NO

# Move Snake in current direction
def move():
    # Get new Coordinates
    for case in switch(DIRECTION):
        if case(RIGHT):
            x_new = x[len(x)-1]+1
            break
        if case(DOWN):
            y_new = y[len(y)-1]+1
            break
        if case(LEFT):
            x_new = x[len(x)-1]-1
            break
        if case(UP):
            y_new = y[len(y)-1]-1
            break

    # Game Over Check - Self Eaten
    for i in range(LED_COLUMN_COUNT):
        if x[i] == x_new:
            if y[i] == y_new:
                STATE = OVER

    # Game Over Check - Boundry
    if (x_new >= LED_COLUMN_COUNT or x_new < 0):
        STATE = OVER
    if (y_new >= LED_COUNT/LED_COLUMN_COUNT or y_new < 0):
        STATE = OVER

    # Check if Apple got Eaten
    if (apple[0] == x_new) and (apple[1] == y_new):
        x.append(x_new)
        y.append(y_new)
        newApple()
    else:
        for i in range(len(x)-1):
            x[i] = x[i+1]
            y[i] = y[i+1]
        x[len(x)-1] = x_new
        y[len(y)-1] = y_new

# Main function
def snake(strip,parameters):
    snake_color = parameters[1]
    apple_color = parameters[2]

    # Main Game Loop
    while True:
        pass
#        for case in switch(STATE):
#            if case(RUNNING):
#                pass
