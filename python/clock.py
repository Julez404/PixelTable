# import time module

import time
from number import setNumber
from getClockParameters import getNumberOne
from getClockParameters import getNumberTwo
from switchcase import switch
from command import CommandsAvailable
from pixels import clearPixelBuffer
from command import delLastCommand
from command import getCommand
from readback import readbackSet
from switchcase import switch

def clock(strip,parameters):
    #löschen
    clearPixelBuffer(strip)

    hours = time.strftime("%H")
    minutes = time.strftime("%M")

    #set Doppelpunkt
    Offset_x = 0
    Offset_y = 0
    ziffer = 10
    setNumber(strip, 0, 0, ziffer, parameters[1])

    compare_ziffer_1 = 0
    compare_ziffer_2 = 0
    compare_ziffer_3 = 0
    compare_ziffer_4 = 0

    ziffer_1 = getNumberOne(int(hours))
    ziffer_2 = getNumberTwo(int(hours) - (ziffer_1 * 10))
    ziffer_3 = getNumberOne(int(minutes))
    ziffer_4 = getNumberTwo(int(minutes) - (ziffer_3 * 10))

    setNumber(strip, 0, 0, ziffer_1, parameters[1])
    setNumber(strip, 0, 4, ziffer_2, parameters[1])
    setNumber(strip, 0, 11, ziffer_3, parameters[1])
    setNumber(strip, 0, 15, ziffer_4, parameters[1])

    while True:


        # print current date and time
        hours = time.strftime("%H")
        minutes = time.strftime("%M")


        #set erste Ziffer
        Offset_x = 0
        Offset_y = 0
        zahl = int(hours)
        ziffer_1 = getNumberOne(zahl)
        if(compare_ziffer_1 != ziffer_1):
            setNumber(strip, Offset_x, Offset_y, compare_ziffer_1, "000000")
            setNumber(strip, Offset_x, Offset_y, ziffer_1, parameters[1])
        compare_ziffer_1 = ziffer_1

        #set zweite Ziffer
        Offset_x = 0
        Offset_y = 4
        zahl = zahl - (ziffer_1 * 10)
        ziffer_2 = getNumberTwo(zahl)
        if(compare_ziffer_2 != ziffer_2):
            setNumber(strip, Offset_x, Offset_y, compare_ziffer_2, "000000")
            setNumber(strip, Offset_x, Offset_y, ziffer_2, parameters[1])
        compare_ziffer_2 = ziffer_2

        #set dritte Ziffer
        Offset_x = 0
        Offset_y = 11
        zahl = int(minutes)
        ziffer_3 = getNumberOne(zahl)
        if(compare_ziffer_3 != ziffer_3):
            setNumber(strip, Offset_x,Offset_y, compare_ziffer_3, "000000")
            setNumber(strip, Offset_x, Offset_y, ziffer_3, parameters[1])
        compare_ziffer_3 = ziffer_3

        #set vierte Ziffer
        Offset_x = 0
        Offset_y = 15
        zahl = zahl - (ziffer_3 * 10)
        ziffer_4 = getNumberTwo(zahl)
        if(compare_ziffer_4 != ziffer_4):
            setNumber(strip, Offset_x, Offset_y, compare_ziffer_4, "000000")
            setNumber(strip, Offset_x, Offset_y, ziffer_4, parameters[1])
        compare_ziffer_4 = ziffer_4


        if int(CommandsAvailable()) > 1:
            break




def showTimer(strip,parameters):
    #löschen
    clearPixelBuffer(strip)

    ziffer_1 = getNumberOne(int(parameters[2]))
    ziffer_2 = int(parameters[2]) - 10*ziffer_1
    ziffer_3 = getNumberOne(int(parameters[3]))
    ziffer_4 = int(parameters[3]) - 10*ziffer_3
    ziffer_5 = getNumberOne(int(parameters[4]))
    ziffer_6 = int(parameters[4]) - 10*ziffer_5

    compare_ziffer_1 = getNumberOne(int(parameters[2]))
    compare_ziffer_2 = int(parameters[2]) - 10*ziffer_1
    compare_ziffer_3 = getNumberOne(int(parameters[3]))
    compare_ziffer_4 = int(parameters[3]) - 10*ziffer_3
    compare_ziffer_5 = getNumberOne(int(parameters[4]))
    compare_ziffer_6 = int(parameters[4]) - 10*ziffer_5

    if((ziffer_1 == 0) and (ziffer_2 == 0)):
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

    compare_sekunde = 0
    while True:
        #time.sleep(0.77)
        sekunde = int(time.strftime("%S")) - 10 * getNumberOne(int(time.strftime("%S")))
        if(compare_sekunde != sekunde):
            compare_sekunde = sekunde
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
                    setNumber(strip, 0, 0, compare_ziffer_3, "000000")
                    setNumber(strip, 0, 0, ziffer_3, parameters[1])
                    compare_ziffer_3 = ziffer_3
                if(compare_ziffer_4 != ziffer_4):
                    setNumber(strip, 0, 4, compare_ziffer_4, "000000")
                    setNumber(strip, 0, 4, ziffer_4, parameters[1])
                    compare_ziffer_4 = ziffer_4
                if(compare_ziffer_5 != ziffer_5):
                    setNumber(strip, 0, 11, compare_ziffer_5, "000000")
                    setNumber(strip, 0, 11, ziffer_5, parameters[1])
                    compare_ziffer_5 = ziffer_5
                if(compare_ziffer_6 != ziffer_6):
                    setNumber(strip, 0, 15, compare_ziffer_6, "000000")
                    setNumber(strip, 0, 15, ziffer_6, parameters[1])
                    compare_ziffer_6 = ziffer_6


            else:
                setNumber(strip, 0, 0, 10, parameters[1])
                if(compare_ziffer_1 != ziffer_1):
                    setNumber(strip, 0, 0, compare_ziffer_1, "000000")
                    setNumber(strip, 0, 0, ziffer_1, parameters[1])
                    compare_ziffer_1 = ziffer_1
                if(compare_ziffer_2 != ziffer_2):
                    setNumber(strip, 0, 4, compare_ziffer_2, "000000")
                    setNumber(strip, 0, 4, ziffer_2, parameters[1])
                    compare_ziffer_2 = ziffer_2
                if(compare_ziffer_3 != ziffer_3):
                    setNumber(strip, 0, 11, compare_ziffer_3, "000000")
                    setNumber(strip, 0, 11, ziffer_3, parameters[1])
                    compare_ziffer_3 = ziffer_3
                if(compare_ziffer_4 != ziffer_4):
                    setNumber(strip, 0, 15, compare_ziffer_4, "000000")
                    setNumber(strip, 0, 15, ziffer_4, parameters[1])
                    compare_ziffer_4 = ziffer_4

        #schauen, ob ein Command noch eingetroffen ist
        if int(CommandsAvailable()) > 1:
            delLastCommand()
            command = getCommand()
            if command[0] == ("stopTimer"):
               readbackSet("~"+str(ziffer_1)+str(ziffer_2)+"~"+str(ziffer_3)+str(ziffer_4)+"~"+str(ziffer_5)+str(ziffer_6)+"~")
               delLastCommand()
            break





def showAlarmClock(strip, parameters):

    #löschen
    clearPixelBuffer(strip)

    #set Doppelpunkt
    Offset_x = 0
    Offset_y = 0
    ziffer = 10
    setNumber(strip, Offset_x, Offset_y, ziffer, parameters[1])

    #set erste Ziffer
    Offset_x = 0
    Offset_y = 0
    zahl = int(parameters[2])
    ziffer_1 = getNumberOne(zahl)
    setNumber(strip, Offset_x, Offset_y, ziffer_1, parameters[1])

    #set zweite Ziffer
    Offset_x = 0
    Offset_y = 4
    zahl = zahl - (ziffer_1 * 10)
    ziffer_2 = getNumberTwo(zahl)
    setNumber(strip, Offset_x, Offset_y, ziffer_2, parameters[1])

    #set dritte Ziffer
    Offset_x = 0
    Offset_y = 11
    zahl = int(parameters[3])
    ziffer_3 = getNumberOne(zahl)
    setNumber(strip, Offset_x, Offset_y, ziffer_3, parameters[1])

    #set vierte Ziffer
    Offset_x = 0
    Offset_y = 15
    zahl = zahl - (ziffer_3 * 10)
    ziffer_4 = getNumberTwo(zahl)
    setNumber(strip, Offset_x, Offset_y, ziffer_4, parameters[1])




def showStopWatch(strip, parameters):
    #löschen
    clearPixelBuffer(strip)

    RUNNING = 0
    STOPPED = 1
    END = 2
    STATE = RUNNING

    ziffer_1 = 0
    ziffer_2 = 0
    ziffer_3 = 0
    ziffer_4 = 0
    ziffer_5 = 0
    ziffer_6 = 0

    compare_ziffer_1 = 5
    compare_ziffer_2 = 9
    compare_ziffer_3 = 0
    compare_ziffer_4 = 0
    compare_ziffer_5 = 0
    compare_ziffer_6 = 0


    setNumber(strip, 0, 0, 10, parameters[1])
    setNumber(strip, 0, 0, ziffer_1, parameters[1])
    setNumber(strip, 0, 4, ziffer_2, parameters[1])
    setNumber(strip, 0, 11, ziffer_3, parameters[1])
    setNumber(strip, 0, 15, ziffer_4, parameters[1])

    compare_sekunde = 0
    while ((STATE == RUNNING) or (STATE == STOPPED)):
        for case in switch(STATE):
            if case(RUNNING):

                #time.sleep(1)
                sekunde = int(time.strftime("%S")) - 10 * getNumberOne(int(time.strftime("%S")))
                if(compare_sekunde != sekunde):
                    compare_sekunde = sekunde
                    if(ziffer_6 < 9):
                        ziffer_6 = ziffer_6 + 1

                    elif(ziffer_6 == 9):
                        ziffer_6 = 0

                        if(ziffer_5 < 5):
                            ziffer_5 = ziffer_5 + 1

                        elif(ziffer_5 == 5):
                            ziffer_5 = 0

                            if(ziffer_4 < 9):
                                ziffer_4 = ziffer_4 + 1

                            elif(ziffer_4 == 9):
                                ziffer_4 = 0

                                if(ziffer_3 < 5):
                                    ziffer_3 = ziffer_3 + 1

                                elif(ziffer_3 == 5):
                                    ziffer_3 = 0

                                    if(ziffer_2 < 9):
                                        ziffer_2 = ziffer_2 + 1

                                    elif(ziffer_2 == 9):
                                        ziffer_2 = 0

                                        if(ziffer_1 < 9):
                                            ziffer_1 = ziffer_1 + 1

                                        else:
                                            break


                    if((ziffer_1 == 0) and (ziffer_2 == 0)):

                        setNumber(strip, 0, 0, 10, parameters[1])
                        if(compare_ziffer_3 != ziffer_3):
                            setNumber(strip, 0, 0, compare_ziffer_3, "000000")
                            setNumber(strip, 0, 0, ziffer_3, parameters[1])
                            compare_ziffer_3 = ziffer_3
                        if(compare_ziffer_4 != ziffer_4):
                            setNumber(strip, 0, 4, compare_ziffer_4, "000000")
                            setNumber(strip, 0, 4, ziffer_4, parameters[1])
                            compare_ziffer_4 = ziffer_4
                        if(compare_ziffer_5 != ziffer_5):
                            setNumber(strip, 0, 11, compare_ziffer_5, "000000")
                            setNumber(strip, 0, 11, ziffer_5, parameters[1])
                            compare_ziffer_5 = ziffer_5
                        if(compare_ziffer_6 != ziffer_6):
                            setNumber(strip, 0, 15, compare_ziffer_6, "000000")
                            setNumber(strip, 0, 15, ziffer_6, parameters[1])
                            compare_ziffer_6 = ziffer_6


                    else:
                        setNumber(strip, 0, 0, 10, parameters[1])
                        if(compare_ziffer_1 != ziffer_1):
                            setNumber(strip, 0, 0, compare_ziffer_1, "000000")
                            setNumber(strip, 0, 0, ziffer_1, parameters[1])
                            compare_ziffer_1 = ziffer_1
                        if(compare_ziffer_2 != ziffer_2):
                            setNumber(strip, 0, 4, compare_ziffer_2, "000000")
                            setNumber(strip, 0, 4, ziffer_2, parameters[1])
                            compare_ziffer_2 = ziffer_2
                        if(compare_ziffer_3 != ziffer_3):
                            setNumber(strip, 0, 11, compare_ziffer_3, "000000")
                            setNumber(strip, 0, 11, ziffer_3, parameters[1])
                            compare_ziffer_3 = ziffer_3
                        if(compare_ziffer_4 != ziffer_4):
                            setNumber(strip, 0, 15, compare_ziffer_4, "000000")
                            setNumber(strip, 0, 15, ziffer_4, parameters[1])
                            compare_ziffer_4 = ziffer_4

                if (int(CommandsAvailable()) > 1):
                    delLastCommand()
                    command = getCommand()
                    if command[0] == "setStopwatch":
                        STATE = RUNNING
                    elif command[0] == "resetStopwatch":
                        clearPixelBuffer(strip)
                        setNumber(strip, 0, 0, 0, parameters[1])
                        setNumber(strip, 0, 4, 0, parameters[1])
                        setNumber(strip, 0, 11, 0, parameters[1])
                        setNumber(strip, 0, 15, 0, parameters[1])
                        ziffer_1 = 0
                        ziffer_2 = 0
                        ziffer_3 = 0
                        ziffer_4 = 0
                        ziffer_5 = 0
                        ziffer_6 = 0
                        compare_ziffer_1 = 0
                        compare_ziffer_2 = 0
                        compare_ziffer_3 = 0
                        compare_ziffer_4 = 0
                        compare_ziffer_5 = 0
                        compare_ziffer_6 = 0
                    elif command[0] == "stopStopwatch":
                        STATE = STOPPED
                    else:
                        STATE = END
                break

            if case(STOPPED):
                if (int(CommandsAvailable()) > 1):
                    delLastCommand()
                    command = getCommand()
                    if command[0] == "setStopwatch":
                        STATE = RUNNING
                    elif command[0] == "resetStopwatch":
                        clearPixelBuffer(strip)
                        setNumber(strip, 0, 0, 0, parameters[1])
                        setNumber(strip, 0, 4, 0, parameters[1])
                        setNumber(strip, 0, 11, 0, parameters[1])
                        setNumber(strip, 0, 15, 0, parameters[1])
                        ziffer_1 = 0
                        ziffer_2 = 0
                        ziffer_3 = 0
                        ziffer_4 = 0
                        ziffer_5 = 0
                        ziffer_6 = 0
                        compare_ziffer_1 = 0
                        compare_ziffer_2 = 0
                        compare_ziffer_3 = 0
                        compare_ziffer_4 = 0
                        compare_ziffer_5 = 0
                        compare_ziffer_6 = 0
                    elif command[0] == "stopStopwatch":
                        pass
                    else:
                        STATE = END
                break
