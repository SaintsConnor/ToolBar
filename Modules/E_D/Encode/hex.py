str = input("Enter item to be HEX endcoded: ")

# pass the str to the int () to convert it into base16 int

base16INT = int(str, 16)

hex_value = hex(base16INT)

# chcking the type of the value

print(type(hex_value))
