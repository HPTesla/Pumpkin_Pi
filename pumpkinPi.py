#!/usr/bin/python -tt
#  PumpkinPi, an LED Jack O'Lantern for Raspberry Pi
#  https://github.com/begillespie/Pumpkin_Pi

#  To access the GPIO on the Raspberry Pi, you must run this program as root.

#  by Brian Gillespie, 2012
#     @begillespie
#  GPL license, see README for more details.

import RPi.GPIO as GPIO, sys, time, random, bigletters

debug = False

#  bigletters is a custom module that prints characters made of ascii art to the console. 
#  Call it using bigletters.write('message','color','style').
#  Run './bigletters.py --h' at the command prompt for a list of options.

pumpkin = ["\033[0;33m",                    # Just a little fun. The color and escape sequences
r"                                .-'\ ",   # should work in BASH. Can't guarantee any other shells.
r"                                \:. \ ",
r"                                |:.  \ ",
r"                                /::'  \ ",
r"                             __/:::.   \ ",
r"                     _.-'-.'`  `'.-'`'._\-'`';.-'-, ",
r"                  .`;    :      :     :      :   : `. ",
r"                 / :     :      :                 :  \ ",
r"                /        :/\          :   /\ :     :  \ ",
r"               ;   :     /\ \   :     :  /\ \      :   ; ",
r"              .    :    /  \ \          /  \ \          . ",
r"              ;        /_)__\ \ :     :/_)__\ \    :    ; ",
r"             ;         `-----`' : ,   :`-----`'          ; ",
r"             |    :      :       / \         :     :     | ",
r"             |                  / \ \ :            :     | ",
r"             |    :      :     /___\ \:      :           | ",
r"             |    :      :     `----`'       :           | ",
r"             ;        |;-.,__   :     :   __.-'|   :     ; ",
r"              ;    :  ||   \ \``/'---'\`\` /  ||        ; ",
r"               .    :  \\   \_\/       \_\/   //   '   . ",
r"                ;       \'._    /\     /\ _.-'/   :   ; ",
r"                 \   :   `._`'-/ /\._./ /\  .'  :    / ",
r"                  `\  :     `-.\/__\__\/_.;'   :   /` ",
r"              jgs   `\  '   :   :        :   :  /` ",
r"                      `-`.__`        :   :__.'-` ",
r"                            `-..`.__.'..-` ",
'\033[0m']    # Pumpkin ASCII art courtesy of The Internet. Thanks, jgs!!

class LED:
  """Access the LEDs with some simple methods"""
  def __init__(self, pin):
    self.pin = pin                      # Initialize the LED object with the pin number
    leds.append(self)                   # The object appends itself to the led list,making
#                                         it easy to perform actions on all the leds at once.
    GPIO.setup(self.pin), GPIO.OUT)     # Set the GPIO pin
  def on(self):
    GPIO.output(self.pin, True)
  def off(self):
    GPIO.output(self.pin, False)

leds = []     # Holds a list of all the LED objects

RedLED = LED(18)
White1LED = LED(23)
White2LED = LED(24)

#  set up GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(motionsensor, GPIO.IN)

motionsensor = 11    # assign GPIO pin for the motion sensor
      
def pumpkin_pi_on():
  if debug: print 'All on'
  for i in range(len(leds)):
    leds[i].on()

def pumpkin_pi_off():
  if debug: print 'All off'
  for i in range(len(leds)):
    leds[i].off()

#  Define some different LED flash patterns. I tried to make each one around 1-2
#  seconds long so the motion sensor gets polled every second or two.
def flash_1(): 
  if debug: print 'Flash 1'
  for i in range(6):
    pumpkin_pi_on()
    sleep.sleep(.25)
    pumpkin_pi_off()
    sleep.sleep(.25)

def flash_2():
  if debug: print 'Flash 2'
  RedLED.on()
  for i in range(6):
    White1LED.on()
    sleep.sleep(.2)
    White2LED.on()
    sleep.sleep(.1)
    White1LED.off()
    White2LED.off()
    sleep.sleep(.2)
  RedLED.off()

def flash_3():
  if debug: print 'Flash 3'
  RedLED.on()
  for i in range(8):
    White1LED.on()
    sleep(.1)
    White1LED.off()
    sleep(.15)
  RedLED.off()

def flash_4():
  if debug: print 'Flash 4'
  for i in range(2):
    White1LED.on()
    sleep.sleep(.5)
    White2LED.on()
    sleep.sleep(.5)
    White1LED.off()
    sleep.sleep(.5)
    White2LED.off()
    sleep.sleep(.5)


# This list is used to randomly call flashing patterns. If you add any pattern
# functions that you want in the rotation, add them to this list.
flash_patterns = [flash_1, flash_2, flash_3, flash_4]     #<-- A list of functions!!

def motion_sequence():     #  Special sequence to call on motion sensor activation
  print 'Motion Sensor Activate'  #debug
  pumpkin_pi_off()
  time.sleep(1)
  pumpkin_pi_on()
  time.sleep(2)
  # do some more stuff

def pumpkin_pi_quit():
      print 'Exit PumpkinPi\n\n'
      for i in range(4):
        pumpkin_pi_on()
        sleep.sleep(1)
        pumpkin_pi_off()
        sleep.sleep(1)
      GPIO.cleanup()
      bigletters.write('      happy', 'yellow', 'normal')     # Print an adorable exit message
      bigletters.write(' halloween!!!', 'yellow', 'normal')
      sys.exit(0)
      
def pumpkin_pi(stopTime):
  while stopTime > time.time():
    if GPIO.input(motionsensor): # Check the motion sensor to show a special animation to visitors.
      motion_sequence()
    else:
      random.choice(flash_patterns)()  # Randomly choose a function from the list and execute it.
      pumpkin_pi_off()
  pumpkin_pi_quit()


def main():
  helpMessage = 'Usage: sudo . /pumpkinPi REQUIRED duration:[hh:mm] OPTIONAL debug mode:{--d}'
 
  if len(sys.argv) == 1:
   print helpMessage
   sys.exit(0)
  if '--d' in sys.argv:
    debug = True

  if len(sys.argv[1]) != 5:
    print helpMessage
    sys.exit(1)
  else:
    hour = int(sys.argv[1][:2])
    minute = int(sys.argv[1][-2:])                     # Convert the duration to seconds and add to
    stopTime = time.time() + (hour * 3600 + minute * 60)  # the current time to find the stop time.

    print 'Jack-O-Lantern will go out at', time.strftime('%H:%M, %B %d, %Y', time.localtime(stopTime))
    print '\033[1;31mUse ctrl+C to exit early.\033[0m'
    
  for line in pumpkin:    # Print a pumpkin to the console.
    print line
  bigletters.write(r' pumpkin*', 'purple', 'bold')

  stopTime = time.time() + 5 #debug
  pumpkin_pi(stopTime)

if __name__ == '__main__':
  print 'PumpkinPi starting'
  main()
