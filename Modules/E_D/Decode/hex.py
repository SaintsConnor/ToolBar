hexstring = input("Enter hex string to be decoded: ")
a_string = bytes.fromhex(hexstring)
a_string = a_string.decode("ascii")
print(a_string)
