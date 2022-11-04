import html

a_string = input("What is to be HTML encoded? ")
encoded_string = html.escape(a_string)

print(encoded_string)
