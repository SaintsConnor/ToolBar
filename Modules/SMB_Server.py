#!/usr/bin/env python
# Copyright (c) 2003-2016 CORE Security Technologies
#
# This software is provided under under a slightly modified version
# of the Apache Software License. See the accompanying LICENSE file
# for more information.
#
# Simple SMB Server example.
#
# Author:
#  Alberto Solino (@agsolino) - Accredited for most of code
#  Connor ( @SaintsConnor )

import sys
import logging

from impacket.examples import logger
from impacket import smbserver, version

if __name__ == '__main__':

    # Init the example's logger theme
    logger.init()
    print version.BANNER

    shareName = input("Name of the share: ")
    comment = input("share's comment to display when asked for shares (Can be left blank): ")
    
    choice = ""
    sharePath == ""
    while sharePath == "" :
    print("Choice directory to host.")
    print("1 - Default Linux Priv Esc")
    print("2 - Default Windows Priv Esc")
    print("3 - Custom")
    choice = input("Enter choice: ")
    if choice == "1" :
        dirchoice = "./Premade_Examples/PrivEsc/Linux/"
    elif choice == "2" :
        dirchoice = "./Premade_Examples/PrivEsc/Windows/"
    elif choice == "3" :
        dirchoice = input("Enter directory from your home folder (EG: ~/Documents/): ")
    else:
        print("Invalid choice")
                    
    try:
    except Exception, e:
       logging.critical(str(e))
       sys.exit(1)

    server = smbserver.SimpleSMBServer()

    server.addShare(shareName.upper(), sharePath, comment)
    server.setSMB2Support(False)
   
    # Here you can set a custom SMB challenge in hex format
    # If empty defaults to '4141414141414141'
    # (remember: must be 16 hex bytes long)
    # e.g. server.setSMBChallenge('12345678abcdef00')
    server.setSMBChallenge('')

    # If you don't want log to stdout, comment the following line
    # If you want log dumped to a file, enter the filename
    server.setLogFile('')

    # Rock and roll
    server.start()
