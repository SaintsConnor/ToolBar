#!/bin/python3

# ------- Notes ------- 
# Please contact Connor if any questions, details listed below

# ------- Author Info -------

# Github.com/SaintsConnor
# Discord: connor#2597
# Email: venomsneakymc@gmail.com

import sys
from datetime import datetime as dt
import socket


target = socket.gethostbyname(input("Enter IP of target: ")) # translates host to ipv4

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
