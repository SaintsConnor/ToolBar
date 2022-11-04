from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

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
     
# The port the FTP server will listen on.
# This must be greater than 1023 unless you run this script as root.
FTP_PORT = 2121

# The name of the FTP user that can log in.
FTP_USER = "Guest"

# The FTP user's password.
FTP_PASSWORD = "password"

# The directory the FTP user will have full read/write access to.
FTP_DIRECTORY = dirchoice


def main():
    authorizer = DummyAuthorizer()

    # Define a new user having full r/w permissions.
    authorizer.add_user(FTP_USER, FTP_PASSWORD, FTP_DIRECTORY, perm='elradfmw')

    handler = FTPHandler
    handler.authorizer = authorizer

    # Define a customized banner (string returned when client connects)
    handler.banner = "pyftpdlib based ftpd ready."

    # Optionally specify range of ports to use for passive connections.
    #handler.passive_ports = range(60000, 65535)

    address = ('', FTP_PORT)
    server = FTPServer(address, handler)

    server.max_cons = 256
    server.max_cons_per_ip = 5

    server.serve_forever()


if __name__ == '__main__':
    main()
    
    print("FTP Server running on your pc @ port 2121.")
    print("Username: Guest")
    print("Password: password")
