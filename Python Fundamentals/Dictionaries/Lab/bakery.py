elements = input().split(" ")

bakery = {}

for item in range(0, len(elements), 2):
    key = elements[item]
    value = int(elements[item + 1])
    bakery[key] = value
print(bakery)
