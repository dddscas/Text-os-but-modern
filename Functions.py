import datetime

# Get the current time in EST
import os
import os.path
import sys
import time
import re

from pytz import timezone
#######################################
# Constants
Delaytime2 = 0.01

##########################################################

def cmdHelp():
  '''Prints all commands'''
  
  print("Commands:")
  print("1. help")
  time.sleep(Delaytime2)
  print("2. time")
  time.sleep(Delaytime2)
  print("3. clear")
  time.sleep(Delaytime2)
  print("4. history")
  time.sleep(Delaytime2)
  print("5. exit")
  time.sleep(Delaytime2)
  print("6. echo {arg}")
  time.sleep(Delaytime2)
  print("7. wait {arg}")
  time.sleep(Delaytime2)
  print("8. touch")
  time.sleep(Delaytime2)
  print("9. reboot")
  time.sleep(Delaytime2)
  print("10. Capture {arg}")
  time.sleep(Delaytime2)
  print("11. Release {arg}")
  time.sleep(Delaytime2)
  print("12. Apprehend {arg}")
  time.sleep(Delaytime2)
  print("13. Deapprehend {arg}")
#end of help
def cmdTime():
  '''current time and date'''
  
  now = datetime.datetime.now(timezone('US/Eastern'))
  print(now.strftime("Date:"+"%B %d, %Y"+" Time:"+" %I:%M %p"+"\n"))
#end of time
def cmdClear():
  '''Clear all text in the console'''
  
  os.system("clear")
#end of clear
def cmdHistory(user):
  '''Prints user history'''
  
  print(user['History'])
#end of history
def cmdExit():
  '''This function exits the program'''
  
  print("See you later!")
  time.sleep(0.5)
  sys.exit()
#end of quit

def cmdEcho(input):
  """Prints the input after typing echo input."""
  
  echoStr = ' '.join(input)
  print(echoStr)
#end of echo

def cmdWait(num):
  ''' Wait for an amount of time '''
  """Corrected by Jaredcat on discord"""
  waittime = num[0]

  if f'{waittime}'.isdigit() and int(waittime) > 0:
    time.sleep(int(waittime))
  else:
    print("Value cannot be zero or lower")
#end of wait

def cmdTouch():
  """Creates an empty file with the specified name."""
  """Corrected by @BenjaminYandon on repl"""
  
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

#end of touch
def cmdReboot():
  """Reboots the system."""
  os.system('python redirect.py')
#end of reboot

# Declare the global variable outside the function
capturevalue = 0

def cmdCapture(input, user):
      """Captures a value and adds to it based on user input."""
      global capturevalue
      capturevalue += int(input[0])
      print(capturevalue)
      user['Capture'] = capturevalue
#end of capture

def cmdRelease(input, user):
      """Releases a value and subtracts from it based on user input."""
      global capturevalue
      capturevalue -= int(input[0])
      print(capturevalue)
      user['Capture'] = capturevalue
#end of release

def cmdApprehend(input, user):
      """Apprehends a value and multiplies it based on user input."""
      global capturevalue
      capturevalue *= int(input[0])
      print(capturevalue)
      user['Capture'] = capturevalue
#end of apprehend

def cmdDeapprehend(input, user):
      """Deapprehends a value and divides it based on user input."""
      global capturevalue
      capturevalue /= int(input[0])
      print(capturevalue)
      user['Capture'] = capturevalue
#end of deapprehend
