#!/bin/python3

# ------- Notes -------
# This program has not been optimised. This is a python experiment, if successful development will begin on a shell script equivalent that is more optimized. 
# Please contact Connor if any questions, details listed below

# ------- Author Info -------

# Github.com/SaintsConnor
# Discord: connor#2597
# Email: venomsneakymc@gmail.com

import sys
from datetime import datetime as dt
import socket

if len(sys.argv) == 2:
  target = socket.gethostbyname(sys.argv[1]) # translates host to ipv4
else:
  print("Invalid number of args")
  print("Syntax: python3 PortScanner.py [ip/hostname]")

print("Scannning target: " + target)
print("Time started: " + str(dt.now()))
print('-' * 50)

try:
  for port in range(1,65535):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(0.5)
    result = s.connect_ex((target, port))
    if result == 0:
      print("port {} is open".format(port))
    s.close 
except KeyboardInterrupt:
  print('\nExitting...')
  sys.exit()
except socket.gaierror:
  print("Hostname couldn't be resolved")
  sys.exit()
except socket.error:
  print("Couldn't connect to server")
  sys.exit()
