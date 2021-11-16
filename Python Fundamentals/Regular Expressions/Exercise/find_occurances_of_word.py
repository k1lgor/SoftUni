import re

data = input()
search = input()

words = re.findall(rf"\b{search}\b", data, re.IGNORECASE)

print(len(words))
