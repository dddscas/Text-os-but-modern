import datetime
import os
import sys
import time
import re
from pytz import timezone

# Constants
DELAY_TIME = 0.01

def cmdHelp():
    """Prints all commands."""
    commands = [
        "1. help",
        "2. time",
        "3. clear",
        "4. history",
        "5. exit",
        "6. echo {arg(str/int)}",
        "7. wait {arg(int)}",
        "8. touch",
        "9. reboot",
        "10. Capture {arg(int)}",
        "11. Release {arg(int)}",
        "12. Apprehend {arg(int)}",
        "13. Deapprehend {arg(int)}",
    ]

    for command in commands:
        print(command)
        time.sleep(DELAY_TIME)

def cmdTime():
    """Displays the current time and date."""
    now = datetime.datetime.now(timezone('US/Eastern'))
    print(now.strftime("Date: %B %d, %Y Time: %I:%M %p\n"))

def cmdClear():
    """Clears all text in the console."""
    os.system("clear")

def cmdHistory(user):
    """Prints user history."""
    print(user['History'])

def cmdExit():
    """Exits the program."""
    print("See you later!")
    time.sleep(0.5)
    sys.exit()

def cmdEcho(input):
    """Prints the input after typing echo input."""
    echo_str = ' '.join(input)
    print(echo_str)

def cmdWait(num):
    """Waits for an amount of time."""
    wait_time = num[0]

    if str(wait_time).isdigit() and int(wait_time) > 0:
        time.sleep(int(wait_time))
    else:
        print("Value cannot be zero or lower")

def cmdTouch():
    """Creates an empty file with the specified name."""
    while True:
        try:
            filename = input("Enter the filename: ")
            filename = re.sub(r'\W+', '', filename) + '.txt'
            with open(filename, 'w'):
                pass
            break
        except FileNotFoundError:
            print("Invalid filename. Please try again.")
        except FileExistsError:
            print("File already exists. Please choose a different filename.")

def cmdReboot():
    """Reboots the system."""
    os.system('python redirect.py')

# Global variable
capture_value = 0

def cmdCapture(input, user):
    """Captures a value and adds to it based on user input."""
    global capture_value
    capture_value += int(input[0])
    print(capture_value)
    user['Capture'] = capture_value

def cmdRelease(input, user):
    """Releases a value and subtracts from it based on user input."""
    global capture_value
    capture_value -= int(input[0])
    print(capture_value)
    user['Capture'] = capture_value

def cmdApprehend(input, user):
    """Apprehends a value and multiplies it based on user input."""
    global capture_value
    capture_value *= int(input[0])
    print(capture_value)
    user['Capture'] = capture_value

def cmdDeapprehend(input, user):
    """Deapprehends a value and divides it based on user input."""
    global capture_value
    capture_value /= int(input[0])
    print(capture_value)
    user['Capture'] = capture_value
