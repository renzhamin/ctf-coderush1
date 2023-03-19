import re

f = open("file.txt", "r")
txt = f.read()

# Coderush???????X?

match = re.findall(r'Coderush_?\d{4}X(.*)X', txt)

print("".join(match))
