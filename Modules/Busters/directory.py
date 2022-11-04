# DirectoryBuster

# Author > Connor, credits to: d4xn

# ▼ Imports ▼

import sys
import requests

# ▼ Inputs, args and variables ▼ 

# The arguments

# The variables that we need to run the script successfully
# Then in the main function the value of these variables will change
url = input("Enter URL: ")
ext = input("Enter Extention, can be left blank: ")

# ▼ Functions ▼

'''
This function make the requests and checks the status code of them,
if the status code is equals to 200, 
the program prints in the console the type of request, the full url and status code
'''
def make_request(url, ext):
    with open("./Wordlists/directory/files.txt") as w:
        dirs = w.readlines()

        for d in dirs:
            d = d.replace("\n", "")
            if ext:
                if url[-1] == '/':
                    r_get = requests.get(f'{url}{d}.{ext}')
                    r_post = requests.post(f'{url}{d}.{ext}')
                            
                    if r_get.status_code == 200 or r_get.status_code == 301 or r_get.status_code == 403:
                        print(f'\nGET - {url}{d}.{ext} - {r_get.status_code}')
        
                    elif r_post.status_code == 200 or r_post.status_code == 301 or r_post.status_code == 403:
                        print(f'\nPOST - {url}{d}.{ext} - {r_post.status_code}')
            
                elif url[-1] != '/':
                    r_get = requests.get(f'{url}/{d}.{ext}')
                    r_post = requests.post(f'{url}/{d}.{ext}')
                    if r_get.status_code == 200 or r_get.status_code == 301 or r_get.status_code == 403:
                        print(f'\nGET - {url}/{d}.{ext} - {r_get.status_code}')
                
                    elif r_post.status_code == 200 or r_post.status_code == 301 or r_post.status_code == 403:
                        print(f'\nPOST - {url}/{d}.{ext} - {r_post.status_code}')
            elif not ext:
                if url[-1] == '/':
                    r_get = requests.get(f'{url}{d}')
                    r_post = requests.post(f'{url}{d}')
                            
                    if r_get.status_code == 200 or r_get.status_code == 301 or r_get.status_code == 403:
                        print(f'\nGET - {url}{d} - {r_get.status_code}')
        
                    elif r_post.status_code == 200 or r_post.status_code == 301 or r_post.status_code == 403:
                        print(f'\nPOST - {url}{d} - {r_post.status_code}')
            
                elif url[-1] != '/':
                    r_get = requests.get(f'{url}/{d}')
                    r_post = requests.post(f'{url}/{d}')
                    if r_get.status_code == 200 or r_get.status_code == 301 or r_get.status_code == 403:
                        print(f'\nGET - {url}/{d} - {r_get.status_code}')
                
                    elif r_post.status_code == 200 or r_post.status_code == 301 or r_post.status_code == 403:
                        print(f'\nPOST - {url}/{d} - {r_post.status_code}')         

    # End of the function


def main(url, ext):
    try:
       
        
    if url != '':
        make_request(url, ext)
        
    # End of the function

if __name__ == "__main__":
    # Executing the function 
    main(url, ext)
