import re

data = input()

phone = re.findall(
    "(\+359-2-[0-9]{3}-[0-9]{4}|\+359 2 [0-9]{3} [0-9]{4})\\b", data)
print(', '.join(phone))
