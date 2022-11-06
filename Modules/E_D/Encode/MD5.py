import hashlib

2behashed = input("Enter information to be MD5 Hashed: ")
result = hashlib.md5(2behashed.encode("utf-8")).hexdigest()
print(result)

with open("MD5Hashes.txt", "a") as file:
    file.write(result)
    file.write("\n")
    file.close()
