import re

data = input()
counter = 0
LIST = []

groups = re.finditer(
    r"([@|#])([a-z]{3,})\1\1([a-z]{3,})\1", data, re.IGNORECASE)

for match in groups:
    counter += 1
    a = match.group(2)
    b = match.group(3)
    if a[::] == b[::-1]:
        x = f"{a} <=> {b}"
        LIST.append(x)

if counter == 0:
    print("No word pairs found!")
else:
    print(f"{counter} word pairs found!")
if not LIST:
    print("No mirror words!")
else:
    print(f"The mirror words are:\n{', '.join(LIST)}")
