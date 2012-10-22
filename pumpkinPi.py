#!/usr/bin/python
#  PumpkinPi, an LED Jack-O'-Lantern for Raspberry Pi 
#  https://github.com/begillespie/Pumpkin_Pi

#  To access the GPIO on the Raspberry Pi, you must run this program as root.

#  by Brian Gillespie, 2012
#     @begillespie
#  GPL license, see README for more details.

import RPi.GPIO as GPIO, sys, signal, time, random, bigletters
#  bigletters is a custom module that prints characters made of ascii art to the console. 
#  Call it using bigletters.write('message','color','style').
#  Run './bigletters.py --h' at the command prompt for a list of options.

pumpkin = ["\033[1;33m",                    # Just a little fun. The color and escape sequences
"                                .-'\ ",   # should work in BASH. Can't guarantee any other shells.
"                                \:. \ ",
"                                |:.  \ ",
"                                /::'  \ ",
"                             __/:::.   \ ",
"                     _.-'-.'`  `'.-'`'._\-'`';.-'-, ",
"                   .`;    :      :     :      :   : `. ",
"                  / :     :      :                 :  \ ",
"                 /        :/\          :   /\ :     :  \ ",
"                ;   :     /\ \   :     :  /\ \      :   ; ",
"               .    :    /  \ \          /  \ \          . ",
"               ;        /_)__\ \ :     :/_)__\ \    :    ; ",
"              ;         `-----`' : ,   :`-----`'          ; ",
"              |    :      :       / \         :     :     | ",
"              |                  / \ \ :            :     | ",
"              |    :      :     /___\ \:      :           | ",
"              |    :      :     `----`'       :           | ",
"              ;        |;-.,__   :     :   __.-'|   :     ; ",
"               ;    :  ||   \ \``/'---'\`\` /  ||        ; ",
"                .    :  \\\   \_\/       \_\/   //   '   .   \033[1;32m  .~~.   .~~. \033[1;33m ",
"                 ;       \\'._    /\     /\ _.-'/   :   ;    \033[1;32m '. \ ' ' / .' \033[1;33m",
"                  \   :   `._`'-/ /\._./ /\  .'  :    /     \033[1;35m  .~..~~~..~. \033[1;33m ",
"                   `\  :     `-.\/__\__\/_.;'   :   /`      \033[1;35m : .~.'~'.~. : \033[1;33m ",
"                     `\  '   :   :        :   :  /`        \033[1;35m ~ (   ) (   ) ~ \033[1;33m ",
"                       `-`.__`        :   :__.'-`         \033[1;35m ( : '~'.~.'~' : ) \033[1;33m ",
"                             `-..`.__.'..-`                \033[1;35m ~ .~ (   ) ~. ~ ",
"                                                             (  : '~' :  )  ",
"\033[1;37m                                     Powered by Raspberry Pi \033[1;35m '~ .~~~. ~' ",
"                                                                  '~' "]
    # Pumpkin ASCII art courtesy of All Over The Internet. Thanks, jgs!!
    # Raspberry ASCII art from "b3n" on the Raspberry Pi forums http://www.raspberrypi.org/phpBB3/viewtopic.php?f=2&t=5494

GPIO.setmode(GPIO.BCM)  #     Initialize the Pi
GPIO.setwarnings(False)

class LED:
  """Access the LEDs with some simple methods"""
  def __init__(self, pin):
    self.pin = pin                      # Initialize the LED object with the pin number
    leds.append(self)                   # The object appends itself to the led list,making
                                        #      it easy to perform actions on all the leds at once.
    GPIO.setup(self.pin, GPIO.OUT)      # Set the GPIO pin
  def on(self):
    GPIO.output(self.pin, True)
  def off(self):
    GPIO.output(self.pin, False)

leds = []     # Holds a list of all the LED objects

RedLED = LED(23)
AmberLED = LED(22)
White1LED = LED(24)
White2LED = LED(25)

motionsensor = 17    # Set up the motion sensor
GPIO.setup(motionsensor, GPIO.IN)

def pumpkin_pi_on():
  if verbose: print 'All on'
  for i in range(len(leds)):
    leds[i].on()

def pumpkin_pi_off():
  if verbose: print 'All off'
  for i in range(len(leds)):
    leds[i].off()

#  Define some different LED flash patterns. I tried to make each one only a few
#  seconds long so the motion sensor gets polled every second or two.
def flash_1(): 
  if verbose: print 'Flash 1'
  for i in range(8):
    pumpkin_pi_on()
    time.sleep(0.2)
    pumpkin_pi_off()
    time.sleep(0.2)

def flash_2():
  if verbose: print 'Flash 2'
  RedLED.on()
  for i in range(6):
    White1LED.on()
    time.sleep(0.2)
    White2LED.on()
    time.sleep(0.1)
    White1LED.off()
    White2LED.off()
    time.sleep(0.2)
  RedLED.off()

def flash_3():
  if verbose: print 'Flash 3'
  RedLED.on()
  for i in range(8):
    White1LED.on()
    time.sleep(0.1)
    White1LED.off()
    time.sleep(0.15)
  RedLED.off()

def flash_4():
  if verbose: print 'Flash 4'
  for i in range(2):
    White1LED.on()
    time.sleep(0.5)
    AmberLED.off()
    White2LED.on()
    time.sleep(0.5)
    White1LED.off()
    time.sleep(0.5)
    White2LED.off()
    AmberLED.on()
    time.sleep(0.5)

def flash_5():
  if verbose: print 'Flash 5'
  pumpkin_pi_on()
  time.sleep(3)
  pumpkin_pi_off()
  time.sleep(0.3)

def flash_6():
  if verbose: print 'Flash 6'
  for i in range(5):
    for j in range(15):
      AmberLED.on()
      time.sleep(.05)
      AmberLED.off()
      time.sleep(.05)
    AmberLED.on()
    time.sleep(.08)

def flash_7():
  if verbose: print 'Flash 7'
  for i in range(15):
    if i % 5 == 0:
      AmberLED.on()
    RedLED.on()
    time.sleep(.05)
    RedLED.off()
    time.sleep(.05)
    AmberLED.off()

# This list is used to randomly call flashing patterns. If you add any pattern
# functions that you want in the rotation, add them to this list as well.
flash_patterns = [flash_1, flash_2, flash_3, flash_4, flash_5, flash_6, flash_7]     #<-- A list of functions!!

def motion_sequence():     #  Special sequence to call on motion sensor activation. It is a long sequence to give the PIR time to stabilize.
  if verbose: print 'Motion Sensor Activate'  #debug
  pumpkin_pi_off()
  time.sleep(2)
  pumpkin_pi_on()
  time.sleep(1)
  White1LED.off()
  time.sleep(0.5)
  White2LED.off()
  time.sleep(1)
  RedLED.off()
  time.sleep(0.5)
  AmberLED.off()
  for i in range(13):     # Lucky number 13
    White1LED.on()
    White2LED.on()
    time.sleep(0.1)
    White1LED.off()
    White2LED.off()
    time.sleep(0.25)
  time.sleep(2)
  AmberLED.on()
  for i in range(100):
    White2LED.on()
    time.sleep(0.01)
    White2LED.off()
    time.sleep(0.01)
  RedLED.on()
  for i in range(4):
    White1LED.on()
    time.sleep(.1)
    White1LED.off()
    time.sleep(.5)
  pumpkin_pi_on()
  time.sleep(10)
  White1LED.off()
  time.sleep(5)
  White2LED.off()
  time.sleep(6)
  AmberLED.off()
  pumpkin_pi_off()
  time.sleep(2)

def pumpkin_pi_quit():
  print 'Exit PumpkinPi\n\n'
  bigletters.write('      happy', 'yellow', 'normal')     # Print an adorable exit message
  bigletters.write(' halloween!!!', 'yellow', 'normal')
  for i in range(4):
    pumpkin_pi_on()
    time.sleep(1)
    pumpkin_pi_off()
    time.sleep(.5)
  GPIO.cleanup()
  if not debug: sys.exit(0)

def debug_function():     # Debug mode to check specific functions:
  global debug
  debug = True
  print '\n'
  funcList = {
    1 : ['Flash 1', flash_1],
    2 : ['Flash 2', flash_2],
    3 : ['Flash 3', flash_3],
    4 : ['Flash 4', flash_4],
    5 : ['Flash 5', flash_5],
    6 : ['Flash 6', flash_6],
    7 : ['Flash 7', flash_7],
    8 : ['Motion Sequence', motion_sequence],
    9 : ['All on', pumpkin_pi_on],
    10 : ['All off', pumpkin_pi_off],
    11 : ['Exit Sequence', pumpkin_pi_quit],
    12 : ['Quit', sys.exit]}
  for i in range(1, len(funcList)+1):
    print '%d : %s' %(i, funcList[i][0])

  x = input('Select function => ')
  print '\n'
  funcList[x][1]()
  debug_function()

def pumpkin_pi(stopTime):
  while stopTime > time.time():
#    if GPIO.input(motionsensor): # Check the motion sensor to show a special animation to visitors.
#      motion_sequence()
#    else:
      random.choice(flash_patterns)()  # Randomly choose a function from the list and execute it.
      pumpkin_pi_off()
  pumpkin_pi_quit()

#  Set up a signal handler to catch Ctrl+C from the keyboard and exit gracefully.
def signal_handler(signal, frame):
  print '\nPumpkinPi exit early'
  pumpkin_pi_quit()
signal.signal(signal.SIGINT, signal_handler)

def main():
  global verbose
  verbose = False
  global debug
  debug = False
  helpMessage = 'Usage: sudo ./pumpkinPi [hh:mm] {-d -v}\n\nPARAMETERS:\n  hh:mm - Duration in hours:minutes (not required with -d)\n\nOPTIONS:\n  -d Debug mode\n  -v Verbose'

  if len(sys.argv) == 1:
    print helpMessage
    sys.exit(0)

  if '-v' in sys.argv:
    verbose = True

  if '-d' in sys.argv:
    debug_function()

  if len(sys.argv[1]) != 5:
    print helpMessage
    sys.exit(1)
  else:
    hour = int(sys.argv[1][:2])
    minute = int(sys.argv[1][-2:])                     # Convert the duration to seconds and add
    stopTime = time.time() + (hour * 3600 + minute * 60)  # the current time to find the stop time.
    print 'Jack-O\'-Lantern will go out at', time.strftime('%H:%M, %B %d, %Y', time.localtime(stopTime))
    print '\033[1;31mUse Ctrl+C to exit early.\033[0m'
    
  for line in pumpkin:    # Print a pumpkin to the console.
    print line
  bigletters.write(r'   pumpkin *', 'purple', 'bold')

#  stopTime = time.time() + 5 #debug
  pumpkin_pi(stopTime)

if __name__ == '__main__':
  print 'PumpkinPi starting'
  main()

