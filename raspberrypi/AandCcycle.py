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
    msg=''
    for strip in xrange(8):
      msg += struct.pack('B',strip)
      for i in xrange(48):
        divisor=max(20-(i+offset)%20,1)
        red=int(150/(divisor))
        green=0
        blue=int(200/(divisor))
        msg += CreatePixel(red, blue, green)
      #print(msg)
    Push(msg)
    offset-=0.5 #Overall rate
    if offset<0:
      offset=40
    #time.sleep(.1)
    

if __name__ == '__main__':
  Dance()
