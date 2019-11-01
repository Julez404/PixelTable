import sys

# Check if number is a valid Hex Value
def isHex(number):
    try:
        int(number,16)
        return True
    except:
        return False

# Check for valid integer
def isInt(number):
    try:
        int(number,10)
        return True
    except:
        return False

# Check for expected str length
def strLengthIs(str,size):
    if (len(str) == size):
        return True
    else:
        return False

# Check for valid picture name
def isValidPictureName(name):
    return True
