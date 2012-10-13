#!/usr/bin/python -tt
#  PumpkinPi, an LED Jack O'Lantern for Raspberry Pi
#  To access the GPIO on the Raspberry Pi, you must run this program as root.

import RPi.GPIO as GPIO, sys, time, random, bigletters
#  bigletters is a custom module that prints characters made of ascii art to the console. Call it using bigletters.write('message','color','style'). Run './bigletters.py --h' at the command prompt for a list of options.

#  assign GPIO pins
led = {
'red':18, 
'white1':23,
'white2':24}
motionsensor = 11

#  variables
debug = False
flash_patterns = [1,2,3,4]    # This list is used to randomly call flashing patterns to make the jack o'lantern more interesting.

pumpkin = ["\033[0;33m",           # Just a little fun
r"                                .-'\ ",
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
'\033[0m']      # Pumpkin ASCII art courtesy of The Internet. Thanks, jgs!!

#  set up GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(led['red'], GPIO.OUT)
GPIO.setup(led['white1'], GPIO.OUT)
GPIO.setup(led['white2'], GPIO.OUT)
GPIO.setup(motionsensor, GPIO.IN)

#  define some different LED flash patterns
def flash_1():
  if debug: print 'Flash 1'
def flash_2():
  if debug: print 'Flash 2'
def flash_3():
  if debug: print 'Flash 3'
def flash_4():
  if debug: print 'Flash 4'

def motion_activate():
  if debug:  print 'Motion Sensor Activate'

def jackolantern():
#  if GPIO.input(motionsensor):     # Check the motion sensor to show a special animation to visitors.
#    motion_activate()
#  else:
    pattern = random.choice(flash_patterns)
    if pattern == 1:
      flash_1()
    elif pattern == 2:
      flash_2()
    elif pattern == 3:
      flash_3()
    elif pattern == 4:
      flash_4()

def jackolantern_off():
  if debug: print 'All off'
  for each in led:
    GPIO.output(led[each], False)
#  GPIO.cleanup()

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
    minute = int(sys.argv[1][-2:])
    stopTime = time.time() + (hour * 3600 + minute * 60)     #  Convert the duration to seconds and add it to the current time to find the stop time.
    print 'Jack-O-Lantern will go out at', time.strftime('%H:%M, %B %d, %Y', time.localtime(stopTime))
    print '\033[1;31mUse ctrl+C to exit early.\033[0m'

  for line in pumpkin:    # Print a pumpkin to the console.
    print line
  bigletters.write(r' pumpkin*', 'purple', 'bold')

  stopTime = time.time() + 5 #debug

  while True:     # Loop the code until time runs out.
    if stopTime > time.time():
      jackolantern()
    else:
      print 'Exit PumpkinPi\n\n'
      jackolantern_off()     # Turn off all the LEDs
      bigletters.write('      happy', 'yellow', 'normal')     # Print an adorable exit message
      bigletters.write(' halloween!!!', 'yellow', 'normal')
      sys.exit(0)

if __name__ == '__main__':
  print 'PumpkinPi starting'
  main()

