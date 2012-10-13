#!/usr/bin/python -tt

import sys

dictionary = {
'a':[
'   A    ',
'  A A   ',
' AAAAA  ',
'AA   AA ',
'AA   AA '],

'b':[
'BBBBB  ',
'BB  BB ',
'BBBBB  ',
'BB  BB ',
'BBBBB  '],

'c':[
'  CCCC  ',
' CC  CC ',
'CC      ',
' CC  CC ',
'  CCCC  '],

'd':[
'DDDD   ',
'DD DD  ',
'DD  DD ',
'DD DD  ',
'DDDD   '],

'e':[
'EEEEEE ',
'EE     ',
'EEEE   ',
'EE     ',
'EEEEEE '],

'f':[
'FFFFFF ',
'FF     ',
'FFFF   ',
'FF     ',
'FF     '],

'g':[
'  GGGG   ',
' GG  GG  ',
'GG       ',
' GG   GG ',
'  GGGGGG '],

'h':[
'HH   HH ',
'HH   HH ',
'HHHHHHH ',
'HH   HH ',
'HH   HH '],

'i':[
'IIIIII ',
'  II   ',
'  II   ',
'  II   ',
'IIIIII '],

'j':[
' JJJJJ ',
'   JJ  ',
'   JJ  ',
'J  JJ  ',
' JJJ   '],

'k':[
'KK  KK ',
'KK KK  ',
'KKKK   ',
'KK KK  ',
'KK  KK '],

'l':[
'LL    ',
'LL    ',
'LL    ',
'LL    ',
'LLLLL '],

'm':[
'MM     MM ',
'MMMM MMMM ',
'MM MMM MM ',
'MM  M  MM ',
'MM     MM '],

'n':[
'NN    NN ',
'NNN   NN ',
'NN NN NN ',
'NN   NNN ',
'NN    NN '],

'o':[
' OOOO  ',
'OO  OO ',
'OO  OO ',
'OO  OO ',
' OOOO  '],

'p':[
'PPPPP  ',
'PP  PP ',
'PPPPP  ',
'PP     ',
'PP     '],

'q':[
'  QQQ   ',
'QQ   QQ ',
'QQ   QQ ',
'QQ   QQ ',
'  QQQ Q '],

'r':[
'RRRRR  ',
'RR  RR ',
'RRRRR  ',
'RR RR  ',
'RR  RR '],

's':[
' SSSS  ',
'SS     ',
' SSSS  ',
'    SS ',
' SSSS  '],

't':[
'TTTTTT ',
'  TT   ',
'  TT   ',
'  TT   ',
'  TT   '],

'u':[
'UU  UU ',
'UU  UU ',
'UU  UU ',
'UU  UU ',
' UUUU  '],

'v':[
'VV     VV ',
'VV     VV ',
' VV   VV  ',
'  VV VV   ',
'   VVV    '],

'w':[
'WW     WW ',
'WW     WW ',
'WW  W  WW ',
'WW WWW WW ',
' WW   WW  '],

'x':[
'XX   XX ',
' XX XX  ',
'  XXX   ',
' XX XX  ',
'XX   XX '],

'y':[
'YY    YY ',
' YY  YY  ',
'   YY    ',
'   YY    ',
'   YY    '],

'z':[
'ZZZZZ ',
'   Z  ',
'  Z   ',
' Z    ',
'ZZZZZ '],

'.':[
'    ',
'    ',
'    ',
'... ',
'... '],

',':[
'    ',
'    ',
' ,, ',
' ,, ',
',,  '],

'!':[
' !!  ',
'!!!! ',
' !!  ',
'     ',
' !!  '],

"'":[
"'' ",
"'' ",
"'  ",
"   ",
"   "],

"#":[
'  ## ##  ',
'######## ',
' ## ##   ',
'#######  ',
'## ##    '],

'=':[
'     ',
'     ',
'==== ',
'==== ',
'     '],

'1':[
' 11  ',
'111  ',
' 11  ',
' 11  ',
'1111 '],

'2':[
' 222  ',
'2  22 ',
'  22  ',
' 22   ',
'22222 '],

'3':[
' 333  ',
'33 33 ',
'  33  ',
'33 33 ',
' 333  '],

'4':[
'    4  ',
'  444  ',
' 4 44  ',
'444444 ',
'   44  '],

'5':[
'55555 ',
'5     ',
'5555  ',
'   55 ',
'5555  '],

'6':[
' 6666  ',
'66     ',
'6666   ',
'66  66 ',
' 6666  '],

'7':[
'777777 ',
'   77  ',
'  77   ',
' 77    ',
'77     '],

'8':[
' 8888  ',
'88  88 ',
' 8888  ',
'88  88 ',
' 8888  '],

'9':[
' 9999  ',
'99  99 ',
'  9999 ',
'    99 ',
' 9999  '],

'0':[
' 00000  ',
'00  000 ',
'00 0 00 ',
'000  00 ',
' 00000  '],

' ':[
'    ',
'    ',
'    ',
'    ',
'    '],

'*':[
' ======== ',
'/ ||  ||  ',
'  ||  ||  ',
'  ||  ||  ',
'  ;   ||  ']}

colorList = {
'black':'30',
'red':'31',
'green':'32',
'yellow':'33',
'blue':'34',
'purple':'35',
'cyan':'36',
'white':'37'}

styleList = {
'normal':'0',
'bold':'1'}

def write(text, color, style):
  message = ['','','','','']
  message[0] += '\033[%s;%sm' %(styleList[style], colorList[color])
  for char in text:
    for i in range(5):
      message[i] += dictionary[char][i]
  message[4] += '\033[0m\n'
  for line in message:
    print line

def main():
  if len(sys.argv) < 2:
    print 'Usage: ./bigletters.py ["string"] {color} {style} {--h}'
    print 'Use the "*" character for "Pi"'
    sys.exit(1)
  if '--h' in sys.argv:
    print 'Colors:'
    for key in colorList.keys():
      print key
    print '\nStyles:'
    for key in styleList.keys():
      print key
    print '\nUse the "*" character for "Pi"'
    sys.exit(0)

  text = str(sys.argv[1]).lower()

  if len(sys.argv) == 2:
    sys.argv.append('white')
    color = 'white'
  elif sys.argv[2] not in colorList:
    color = 'white'
  else:
    color = sys.argv[2]

  if len(sys.argv) == 3:
    sys.argv.append('normal')
    style = 'normal'
  elif sys.argv[3] not in styleList:
    style = 'normal'
  else:
    style = sys.argv[3]

  write(text, color, style)

if __name__ == '__main__':
  main()

