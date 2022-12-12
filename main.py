#ToolBar Script
#Author's: Connor

# Import libraries
import os
import update

# Global Variables
choice = ""

# Define Functions
def Update_Script():
  update.Update()

# Main Scripts
Update_Script()
print("If any issues, please contact the development team.")
while choice != "quit":
  print("-"*10, "Main Menu", '-'*10)
  print("Please type the number for one of the following tools momentarily.")
  print("\n")
  print("1 - HTTP Server")
  print("2 - SMB Server. Please note you must know sudo password, and be able to run sudo python3")
  print("3 - FTP Server")
  print("4 - Port Scanner (Coded in Python)")
  print("5 - Network Scanner")
  print("6 - Dictionary Buster")
  print("7 - Subdomain Buster")
  # Still In Development - print("8 - Discord bot hoster (Must be pre-coded)")
  print("9 - Encoder")
  print("10 - Decoder")
  print("11 - Tools Installer")
  choice = input("Please type the number of your associated module: ")
  
  if choice == "1" :
    os.system("python3 ./Modules/HTTP_Server.py")
    
  elif choice == "2" :
    os.system("sudo python3 ./Modules/SMB_Server.py")
    
  elif choice == "3" :
    os.system("python3 ./Modules/FTP_File.py")
    
  elif choice == "4" :
    os.system("python3 ./Modules/PortScanner.py")
    
  elif choice == "5" :
    os.system("python3 ./Modules/netscan.py")
  
  elif choice == "6" :
    os.system("python3 ./Modules/Busters/dictionary.py")
  
  elif choice == "7" :
    os.system("python3 ./Modules/Busters/DNSChecker.py")
  
  elif choice == "8" :
    print("This Feature has not been implemented.")
  
  elif choice == "9" :
    os.system("python3 ./Modules/E_D/Encoder.py")
  
  elif choice == "10" :
    os.system("python3 ./Modules/E_D/Decoder.py")
    
  elif choice == "11":
    os.system("python3 ./Modules/githubcloner.py")
    
  else :
    print("Invalid Selection.")

print("Thank you for using toolbar.")
