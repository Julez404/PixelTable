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

# Check for valid Key input
def isValidKey(key):
    if (
            key == "UP" or
            key == "DOWN" or
            key == "RIGHT" or
            key == "LEFT" or
            key == "A" or
            key == "B"
        ):
        return True
    else:
        return False
