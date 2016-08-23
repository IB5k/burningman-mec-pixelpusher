import struct
import socket
import time
from math import pi, sin

IP_LIST = ['192.168.111.126',
'192.168.111.120',
'192.168.111.121',
'192.168.111.122',
'192.168.111.123',
'192.168.111.124',
'192.168.111.125',
'192.168.111.127']
UDP_PORT = 9897

sequence = 0

def wheel(position):
  position = position % 1532
  red=0
  green=0
  blue=0
  if position<256:
    green=255
    blue=position
    red=0
  elif 255 <= position < 512:
    green=511-position
    blue=255
  elif 512 <= position < 767:
    red=position-512
    blue=255
  elif 767 <= position < 1022:
    blue=1022-position
    red=255
  elif 1022 <= position < 1277:
    green=position-1022
    red=255
  elif 1277 <= position < 1533:
    red=1532-position
    green=255
  return [red,green,blue]

def CreatePixel(red, green, blue):
  packed=struct.pack('BBB',red,green,blue)
  return packed

def Push(messages):
  global sequence
  stack = struct.pack('Bxxx',sequence)+messages
  sock = socket.socket(
    socket.AF_INET, # Internet
    socket.SOCK_DGRAM) # UDP
  for UDP_IP in IP_LIST:
    bytes_sent = sock.sendto(stack, (UDP_IP, UDP_PORT))
  sequence+=1
  if sequence > 255:
      sequence = 0

def Dance():
  increment = 0
  offset=0
  while True:
    increment += .0005
    msg=''
    for strip in xrange(8):
      msg += struct.pack('B',strip)
      for i in xrange(48):
        red,green,blue=wheel(i*30-offset) #Increment per pixel
        msg += CreatePixel(red, green, blue)
      #print(msg)
    Push(msg)
    offset+=10 #Overall rate
    if offset> 1533:
      offset=0
    #time.sleep(.000005)
    

if __name__ == '__main__':
  Dance()
