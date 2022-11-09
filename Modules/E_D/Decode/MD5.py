hashes = []
unhashed = []

with open("../Hashes/MD5Hashes.txt", "r") as file:
    for line in file:
        hashes.append(line.rstrip())
    file.close

with open("../Hashes/MD5Unhashed.txt", "r") as file:
    for line in file:
        unhashed.append(line.rstrip())
    file.close
    
hashed = input("Enter MD5 Hash to be dehashed: ")
list = len(hashes)
checked = 0
while checked < len:
    2bechecked = hashes[checked]
    if 2becheked == hashed:
      print("Success! Your hash is: ", unhashed[checked])
    else:
      print("We do not have this MD5 unhashed! We're really sorry! Please try again soon <3")


    
