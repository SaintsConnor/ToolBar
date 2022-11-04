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
print("-"*10, "Toolbar", '-'*10)
print("Your one stop shop for a variety of tools!")
print("If any issues, please contact the development team.")
while choice != "quit":
  print("-"*10, "Main Menu", '-'*10)
  print("Please type the number for one of the following tools momentarily.")
  print("\n")
  print("1 - HTTP Server")
  print("2 - SMB Server")
  print("3 - FTP Server")
  print("4 - Port Scanner (Coded in Python)")
  print("5 - Network Scanner")
  print("6 - Dictionary Buster")
  # Still In Development - print("7 - Subdomain Buster")
  # Still In Development - print("8 - Discord bot hoster (Must be pre-coded)")
  # Still In Development - print("9 - Encoder")
  # Still In Development - print("10 - Decoder")
  choice = input("Please type the number of your associated module: ")
  
  if choice == "1" :
    os.system("python3 ./Modules/HTTP_Server.py")
    
  elif choice == "2" :
    os.system("python3 ./Modules/SMB_Server.py")
    
  elif choice == "3" :
    os.system("python3 ./Modules/FTP_File.py")
    
  elif choice == "4" :
    os.system("python3 ./Modules/PortScanner.py")
    
  elif choice == "5" :
    os.system("python3 ./Modules/netscan.py")
  
  elif choice == "6" :
    os.system("python3 ./Modules/Busters/dictionary.py")
  
  elif choice == "7" :
    print("This Feature has not been implemented.")
  
  elif choice == "8" :
    print("This Feature has not been implemented.")
  
  elif choice == "9" :
    print("This Feature has not been implemented.")
  
  elif choice == "10" :
    print("This Feature has not been implemented.")
    
  else :
    print("Invalid Selection.")

print("Thank you for using toolbar.")
