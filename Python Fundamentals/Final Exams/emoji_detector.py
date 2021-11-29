import re

data = input()
threshold = 1

match = re.findall(r"\d", data)
for i in match:
    threshold *= int(i)

emoji = [i for i in (x.group()
                     for x in re.finditer(r"(::|\*\*)([A-Z][a-z]{2,})\1", data))]

print(
    f"Cool threshold: {threshold}\n{len(emoji)} emojis found in the text. The cool ones are:")

for i in emoji:
    total = sum(ord(j) for j in i if j not in [":", "*"])
    if total >= threshold:
        print(f"{i}")
