# Libraries
import os 

# Variables
webpage = ""
menuchoice = 0

# Actual Code

while menuchoice != 3 :
  print("-"*10 + "Tool Installer" + "-"*10)
  print("1 - Github Cloner (Already have link)")
  print("2 - SaintsConnor Tools Installer")
  print("3 - Quit")
  menuchoice = input("Enter number for option: ")
  if menuchoice == 1 :
    webpage = input("Enter FULL link to the github repository: ")
    
    exec = webpage
    os.system(exec)
  if menuchoice == 2:
    print("SaintsConnor Tool Installer")
    print("1 - All Scripts")
    print("2 - Github Installer (Linux) & Execute it")
    print("3 - Pentest Box Setup (Linux) & Execute it")
    print("4 - Pentest Scripts/Wordlists")
    toolchoice = input("Enter number for desired option: ")
    if toolchoice == 1:
      os.system("git clone github.com/SaintsConnor/Scripts-Pentest ~/Downloads")
      os.system("git clone github.com/SaintsConnor/Work ~/Downloads")
      os.system("git clone github.com/SaintsConnor/TOOLS-INSTALLER ~/Downloads")
      os.system("git clone github.com/SaintsConnor/Writeups ~/Downloads")
      os.system("git clone github.com/SaintsConnor/KOTHScripts ~/Downloads")
    if toolchoice == 2:
      os.system("git clone github.com/SaintsConnor/TOOLS-INSTALLER ~/Downloads")
      os.system("sudo chmod +x ~/Downloads/TOOLS-INSTALLER/installgithub.sh")
      os.system("sudo ~/Downloads/TOOLS-INSTALLER/installgithub.sh")
    if toolchoice == 3:
      os.system("git clone github.com/SaintsConnor/TOOLS-INSTALLER ~/Downloads")
      os.system("sudo chmod +x ~/Downloads/TOOLS-INSTALLER/installtools.sh")
      os.system("sudo ~/Downloads/TOOLS-INSTALLER/installtools.sh")
    if toolchoice == 4:
      os.system("git clone github.com/SaintsConnor/Scripts-Pentest ~/Downloads")
