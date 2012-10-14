#!/usr/bin/python
#  PumpkinPi, an LED Jack O'Lantern for Raspberry Pi 
#  https://github.com/begillespie/Pumpkin_Pi

#  To access the GPIO on the Raspberry Pi, you must run this program as root.

#  by Brian Gillespie, 2012
#     @begillespie
#  GPL license, see README for more details.

import RPi.GPIO as GPIO, sys, signal, time, random, bigletters
#  bigletters is a custom module that prints characters made of ascii art to the console. 
#  Call it using bigletters.write('message','color','style').
#  Run './bigletters.py --h' at the command prompt for a list of options.

pumpkin = ["\033[0;33m",                    # Just a little fun. The color and escape sequences
r"                                      .-'\ ",   # should work in BASH. Can't guarantee any other shells.
r"                                      \:. \ ",
r"                                      |:.  \ ",
r"                                      /::'  \ ",
r"                                   __/:::.   \ ",
r"                           _.-'-.'`  `'.-'`'._\-'`';.-'-, ",
r"                        .`;    :      :     :      :   : `. ",
r"                       / :     :      :                 :  \ ",
r"                      /        :/\          :   /\ :     :  \ ",
r"                     ;   :     /\ \   :     :  /\ \      :   ; ",
r"                    .    :    /  \ \          /  \ \          . ",
r"                    ;        /_)__\ \ :     :/_)__\ \    :    ; ",
r"                   ;         `-----`' : ,   :`-----`'          ; ",
r"                   |    :      :       / \         :     :     | ",
r"                   |                  / \ \ :            :     | ",
r"                   |    :      :     /___\ \:      :           | ",
r"                   |    :      :     `----`'       :           | ",
r"                   ;        |;-.,__   :     :   __.-'|   :     ; ",
r"                    ;    :  ||   \ \``/'---'\`\` /  ||        ; ",
r"                     .    :  \\   \_\/       \_\/   //   '   . ",
r"                      ;       \'._    /\     /\ _.-'/   :   ; ",
r"                       \   :   `._`'-/ /\._./ /\  .'  :    / ",
r"                        `\  :     `-.\/__\__\/_.;'   :   /` ",
r"                    jgs   `\  '   :   :        :   :  /` ",
r"                            `-`.__`        :   :__.'-` ",
r"                                  `-..`.__.'..-` ",
'\033[0m']    # Pumpkin ASCII art courtesy of The Internet. Thanks, jgs!!

GPIO.setmode(GPIO.BCM)  #     Initialize the Pi
GPIO.setwarnings(False)

class LED:
  """Access the LEDs with some simple methods"""
  def __init__(self, pin):
    self.pin = pin                      # Initialize the LED object with the pin number
    leds.append(self)                   # The object appends itself to the led list,making
#                                         it easy to perform actions on all the leds at once.
    GPIO.setup(self.pin, GPIO.OUT)     # Set the GPIO pin
  def on(self):
    GPIO.output(self.pin, True)
  def off(self):
    GPIO.output(self.pin, False)

leds = []     # Holds a list of all the LED objects

RedLED = LED(18)
White1LED = LED(23)
White2LED = LED(24)

motionsensor = 11    # Set up the motion sensor
GPIO.setup(motionsensor, GPIO.IN)

def pumpkin_pi_on():
  if debug: print 'All on'
  for i in range(len(leds)):
    leds[i].on()

def pumpkin_pi_off():
  if debug: print 'All off'
  for i in range(len(leds)):
    leds[i].off()

#  Define some different LED flash patterns. I tried to make each one only a few
#  seconds long so the motion sensor gets polled every second or two.
def flash_1(): 
  if debug: print 'Flash 1'
  for i in range(6):
    pumpkin_pi_on()
    time.sleep(.25)
    pumpkin_pi_off()
    time.sleep(.25)

def flash_2():
  if debug: print 'Flash 2'
  RedLED.on()
  for i in range(6):
    White1LED.on()
    time.sleep(.2)
    White2LED.on()
    time.sleep(.1)
    White1LED.off()
    White2LED.off()
    time.sleep(.2)
  RedLED.off()

def flash_3():
  if debug: print 'Flash 3'
  RedLED.on()
  for i in range(8):
    White1LED.on()
    time.sleep(.1)
    White1LED.off()
    time.sleep(.15)
  RedLED.off()

def flash_4():
  if debug: print 'Flash 4'
  for i in range(2):
    White1LED.on()
    time.sleep(.5)
    White2LED.on()
    time.sleep(.5)
    White1LED.off()
    time.sleep(.5)
    White2LED.off()
    time.sleep(.5)

def flash_5():
  if debug: print 'Flash 5'
  pumpkin_pi_on()
  time.sleep(3)
  pumpkin_pi_off()

# This list is used to randomly call flashing patterns. If you add any pattern
# functions that you want in the rotation, add them to this list as well.
flash_patterns = [flash_1, flash_2, flash_3, flash_4, flash_5]     #<-- A list of functions!!

def motion_sequence():     #  Special sequence to call on motion sensor activation
  if debug: print 'Motion Sensor Activate'  #debug
  pumpkin_pi_off()
  time.sleep(2)
  pumpkin_pi_on()
  time.sleep(1)
  White1LED.off()
  time.sleep(.5)
  White2LED.off()
  time.sleep(1)
  RedLED.off()
  time.sleep(.5)
  for i in range(13):
    White1LED.on()
    White2LED.on()
    time.sleep(.1)
    White1LED.off()
    White2LED.off()
    time.sleep(.25)

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
  sys.exit(0)
      
def pumpkin_pi(stopTime):
  while stopTime > time.time():
#    if GPIO.input(motionsensor): # Check the motion sensor to show a special animation to visitors.
#      motion_sequence()
#    else:
      random.choice(flash_patterns)()  # Randomly choose a function from the list and execute it.
      pumpkin_pi_off()
  pumpkin_pi_quit()

def signal_handler(signal, frame):
  print '\nPumpkinPi exit early'
  pumpkin_pi_quit()
signal.signal(signal.SIGINT, signal_handler)

def main():
  global debug
  debug = False

  helpMessage = 'Usage: sudo . /pumpkinPi REQUIRED duration:[hh:mm] OPTIONAL debug mode:{--d}'

  if len(sys.argv) == 1:
   print helpMessage
   sys.exit(0)
  if '--d' in sys.argv:
    print 'Found --d flag'
    print debug
    debug = True
    print debug

  if len(sys.argv[1]) != 5:
    print helpMessage
    sys.exit(1)
  else:
    hour = int(sys.argv[1][:2])
    minute = int(sys.argv[1][-2:])                     # Convert the duration to seconds and add t
    stopTime = time.time() + (hour * 3600 + minute * 60)  # the current time to find the stop time.

    print 'Jack-O-Lantern will go out at', time.strftime('%H:%M, %B %d, %Y', time.localtime(stopTime))
    print '\033[1;31mUse Ctrl+C to exit early.\033[0m'
    
  for line in pumpkin:    # Print a pumpkin to the console.
    print line
  bigletters.write(r'   pumpkin *', 'purple', 'bold')

#  stopTime = time.time() + 5 #debug
  pumpkin_pi(stopTime)

if __name__ == '__main__':
  print 'PumpkinPi starting'
  main()

