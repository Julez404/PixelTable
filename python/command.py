import sys

MAX_PARAMETERS = 10

def delFirstLine(file):
    file.seek(0)
    file.readline()
    data = f.read()
    file.seek(0)
    file.write(data)
    file.truncate()
    file.seek(0)


def getCommand():
    f = open("/var/www/pixel/python/.command", "r")
    last_read = f.readline()

    # Check if new Command is there
    if (last_read == ("--COMMAND-BEGIN--" + '\n')):
        iterations = 0
        command = []

        # Read file till COMMAND-END is reached or iteration limit is reached
        last_read = f.readline() # Read Command Name, Valid for all commands
        while ( (last_read != ("--COMMAND-END--" + '\n')) and (iterations < MAX_PARAMETERS) ):
            command.append(last_read)
            last_read = f.readline()

        f.close()

        # Check if reading was successfull or max Limit was reached
        if (last_read == ("--COMMAND-END--" + '\n')):
            return command
        else:
            command = ["NONE"]
            return command

    # No new command -> Return Command array with NONE as command
    else:
        command = ["NONE"]
        return command

def setNewCommand(command):
    f = open("/var/www/pixel/python/.command", "a")
    f.write("--COMMAND-BEGIN--" + '\n')
    for i in command:
        f.write(i+'\n')
    f.write("--COMMAND-END--" + '\n')
    f.close()

def delLastCommand():
    f = open("/var/www/pixel/python/.command", "r+")
    last_read = f.readline()

    while (last_read != ("--COMMAND-END--" + '\n')):
        delFirstLine(f)
        last_read = f.readline()

    delFirstLine(f)
    f.close()
