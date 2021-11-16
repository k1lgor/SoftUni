import re

data = input()
numbers = re.finditer(r"(^|(?<=\s))-?\d+(\.\d+)?($|(?=\s))", data)

for num in numbers:
    print(num.group(), end=' ')
