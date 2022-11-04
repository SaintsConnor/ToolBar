import os
from http.server import HTTPServer, CGIHTTPRequestHandler

choice = ""
dirchoice = ""

while dirchoice == "" :
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

# Make sure the server is created at current directory
os.chdir(dirchoice)
# Create server object listening the port 80
server_object = HTTPServer(server_address=('', 80), RequestHandlerClass=CGIHTTPRequestHandler)
# Start the web server
server_object.serve_forever()

print("Server Started.")
