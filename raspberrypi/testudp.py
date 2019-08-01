import struct
import socket
import time
from math import pi, sin

UDP_IP = '192.168.111.126'
UDP_PORT = 9897

sequence = 0

def sinc(x):
  try:
    x = pi * x
    return sin(x) / x
  except ZeroDivisionError:  # sinc(0) = 1
    return 1.0

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
  print stack.__len__()
  #print message
  sock = socket.socket(
    socket.AF_INET, # Internet
    socket.SOCK_DGRAM) # UDP
  sock.bind(('',6960))
  bytes_sent = sock.sendto(stack, (UDP_IP, UDP_PORT))
  sequence+=1
  if sequence > 255:
      sequence = 0
    #print 'Bytes sent: %d' % bytes_sent

RANGE = pi 

def Dance():
  increment = 0
  while True:
    increment += .005
    start_angle = (increment % (RANGE)) - (RANGE/2)
    #print 'Start angle: %f' % (start_angle)
    msg=''
    for strip in xrange(8):
      msg += struct.pack('B',strip)
      for i in xrange(48):
        offset = (i * pi/180)
        red = ColorFromAngle((start_angle + offset) * 3)
        blue = ColorFromAngle((start_angle + offset) * 2)
        green = ColorFromAngle(start_angle + offset)
        msg += CreatePixel(red, green, blue)
      #print(msg)
    Push(msg)
    time.sleep(.005)
    

if __name__ == '__main__':
  Dance()
