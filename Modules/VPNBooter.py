#Import libraries
import os

#Get User Variables
choice = 0 
THMUser = ""
HTBUser = ""
Path2VPN = ""

#Menu - Base
def main() :
  while choice != 4:
    print("Welcome to VPN Booter")
    print("-"*10)
    print("Disclaimer: You must be on linux and know the sudo password")
    print("Options:")
    print("1 - HTB (Hack The Box)")
    print("2 - THM (TryHackMe)")
    print("3 - Other VPN (Must know the path to .ovpn file)")
    print("4 - Quit")
    choice = input("Enter number associated with your function: ")
  
    if choice = 1:
      HTB()
    elif choice = 2:
      THM()
    elif choice = 3:
      Other()
    else :
      print("Invalid option.")
      choice = 0

#Menu - HTB
def HTB():
  username = input("Enter HTB Username: ")
  path = "~/VPNs/" + username + ".ovpn"
  os.system(path)
  
#Menu - THM

#Menu - Other

#Run Script
main()
