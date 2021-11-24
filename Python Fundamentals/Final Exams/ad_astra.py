import re
from math import floor

data = input()

total_calories = sum(int(x.group(4)) for x in re.finditer(
    r"(\||#)([a-zA-Z\s]+)\1(\d{2}\/\d{2}\/\d{2})\1(\d+)\1", data))

print(f"You have food to last you for: {floor(total_calories / 2000)} days!")

for i in re.finditer(
        r"(\||#)([a-zA-Z\s]+)\1(\d{2}\/\d{2}\/\d{2})\1(\d+)\1", data):
    print(
        f"Item: {i.group(2)}, Best before: {i.group(3)}, Nutrition: {i.group(4)}")
