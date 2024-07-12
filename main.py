# Imports
import datetime
from pytz import timezone

# Get the current time in EST

import json
import os
import os.path
import re
import requests
import sys
import time
import Functions
import getpass
import hashlib
import pyfiglet
from colorama import Fore, Back, Style

osname = "Terminal+"
##############################################
ascii_name = pyfiglet.figlet_format("Terminal+", font="utopia")
##############################################
print(ascii_name)
user = os.environ.get("REPL_OWNER")
terminaldesign = (Fore.LIGHTGREEN_EX + (user if user is not None else "") +
                  Fore.LIGHTBLUE_EX + "@" + Fore.RED + osname +
                  Fore.LIGHTBLUE_EX + "::: ")
##############################################
'''Template for userdata'''
user = {
    "Name": "unknown",
    "History": [],
    "Password": "unknown",
    "Capture": "0"
}
##############################################
'''Contstants'''
DELAYTIME1 = 0.145665432


##############################################
def saveuser():
  with open(filename, 'w') as json_file:
    json.dump(user, json_file)
  json_file.close()


##############################################
print("Welcome, to Terminal+!")
time.sleep(DELAYTIME1)
now = datetime.datetime.now(timezone('US/Eastern'))
#sets timezone
print(now.strftime("Date: " + "%B %d, %Y" + " Time:" + " %I:%M %p" + "\n"))
#prints date and time
time.sleep(DELAYTIME1)
# entername
user['Name'] = input("What's your name? ")
# sanitize username
pattern = re.compile('[\\W_]+')
filename = re.sub(pattern, '', user['Name']) + '.udat'
# check if file exists
if os.path.isfile(filename):
  with open(filename) as f:
    user = json.load(f)
  f.close()
  time.sleep(DELAYTIME1)
  passwordcheck = getpass.getpass(prompt="Please enter your password: ")

  if hashlib.md5(
      passwordcheck.encode('utf-8')).hexdigest() == user['Password']:
    time.sleep(DELAYTIME1)
    print("Welcome back, " + user['Name'])
  else:
    print("Incorrect password, please try again.")
    Functions.cmdReboot()
else:
  # checks if user is new
  print("\nNice to meet you, " + user['Name'])
  # prints welcome
  temppassword = input("Select your password!")
  time.sleep(1)
  confirm = input("Confirm your password!")
  if confirm == temppassword:
    user['Password'] = hashlib.md5(temppassword.encode('utf-8')).hexdigest()
    saveuser()
#encrypts set password
  else:
    print("Passwords do not match!")
    Functions.cmdReboot()
# saves user
#########################################################
while 1:
  time.sleep(DELAYTIME1)
  request = input("What would you like to do? ")
  cmdLine = request.split()
  cmdStr = cmdLine.pop(0)
  #checks for request
  #########################################################
  match cmdStr.lower():
    case "help":
      Functions.cmdHelp()
    case "time":
      Functions.cmdTime()
    case "clear":
      Functions.cmdClear()
    case "history":
      Functions.cmdHistory(user)
    case "exit":
      Functions.cmdExit()
    case "echo":
      Functions.cmdEcho(cmdLine)
    case "wait":
      Functions.cmdWait(cmdLine)
    case "touch":
      Functions.cmdTouch()
    case "reboot":
      Functions.cmdReboot()
    case "capture":
      Functions.cmdCapture(cmdLine, user)
      saveuser()
    case "release":
      Functions.cmdRelease(cmdLine, user)
      saveuser()
    case "apprehend":
      Functions.cmdApprehend(cmdLine, user)
      saveuser()
    case "deapprehend":
      Functions.cmdDeapprehend(cmdLine, user)
      saveuser()
#All other functions above this line
    case _:
      print("Invalid command")
#########################################################
  user['History'].append(request.lower())
  saveuser()
