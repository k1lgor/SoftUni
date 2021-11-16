import re

data = input()
num_list = []

while data:
    nums = re.findall(r"\d+", data)
    num_list.extend(nums)

    data = input()

print(*num_list)
