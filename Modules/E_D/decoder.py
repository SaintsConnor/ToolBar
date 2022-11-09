#Decoder Script
#Author's: Connor

#Lists
algorithms = ['MD5', 'Base64', 'Hex', 'HTML']

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
  print("Please type the number for one of the following algorithms or type search momentarily.")
  print("\n")
  print("1 - MD5")
  print("2 - Base64")
  print("3 - Hex")
  print("4 - HTML")
  print("Search for others")
   
  choice = input("Enter your algorithm number or type 'Search': ")
  
  if choice == '1':
    os.system('python3 ./Decode/MD5.py')
  elif choice == '2':
    os.system('python3 ./Decode/Base64.py')
  elif choice == '3':
    os.system('python3 ./Decode/Hex.py')
  elif choice == '4': 
    os.system('python3 ./Decode/HTML.py')
  elif choice == 'Search':
    search = input("Enter algorithm to check: ")
    if search in algorithms:
      execcommand2berun = "python3 ./Decode/" + search + ".py"
      os.system(execcommand2berun)
    else :
      print("Unfortunately, we do not support that algorithm yet. Please talk with our development team to see if we can this added.")
        
  else :
    print("Invalid Selection.")


