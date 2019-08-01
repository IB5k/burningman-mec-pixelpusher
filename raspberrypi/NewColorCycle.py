import struct
import socket
import time
from math import pi, sin

IP_LIST = ['192.168.111.126',
'192.168.111.121',
'192.168.111.122',
'192.168.111.123',
'192.168.111.124',
'192.168.111.125',
'192.168.111.127']
UDP_PORT = 9897

sequence = 0

def wheel(angle):
	green=int((angle*4.25)%255)
	red=int((angle*4.25-120)%255)
	blue=int((angle*4.25-240)%255)
	return [red,green,blue]

def ColorFromAngle(angle):
  return abs(int(sinc(angle) * 255))

def CreatePixel(red, green, blue):
  packed=struct.pack('BBB',red,green,blue)
  return packed

def Push(messages):
  global sequence
  #assert type(messages) == list
  #stack=''
  #for message in messages:
  #  stack += message
  stack = struct.pack('Bxxx',sequence)+messages
  #print stack.__len__()
  #print message
  sock = socket.socket(
    socket.AF_INET, # Internet
    socket.SOCK_DGRAM) # UDP
  for UDP_IP in IP_LIST:
    bytes_sent = sock.sendto(stack, (UDP_IP, UDP_PORT))
  sequence+=1
  if sequence > 255:
      sequence = 0
    #print 'Bytes sent: %d' % bytes_sent

RANGE = pi

def Dance():
  increment = 0
  offset=0
  while True:
    increment += .0005
    start_angle = (increment % (RANGE)) - (RANGE/2)
    #print 'Start angle: %f' % (start_angle)
    msg=''
    for strip in xrange(8):
      msg += struct.pack('B',strip)
      for i in xrange(48):
        red,green,blue=wheel(i-offset)
        msg += CreatePixel(red, green, blue)
      #print(msg)
    Push(msg)
    offset+=1
    if offset> 360:
      offset=0
    #time.sleep(.000005)
    

if __name__ == '__main__':
  Dance()
