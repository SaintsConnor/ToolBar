import socket

subdomain_list = []
with open('subdomains.txt', 'r') as f:
    subdomains_list = f.read().splitlines()

domain = str(input("Enter domain you wish to enumerate: "))

for subdomain in subdomain_list:
    hostname = subdomain + '.' + domain
    try:
        ip = socket.gethostbyname(hostname)
        print(f'{hostname} has IP address {ip}')
    except socket.gaierror:
        print(f'{hostname} could not be resolved')
