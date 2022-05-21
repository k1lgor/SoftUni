import re

data = input()
furnitures = []
total_result = 0
while data != "Purchase":
    if regex := re.match(r">>(?P<furniture>[A-Za-z]+)<<(?P<price>\d+(\.\d+)?)\!(?P<quantity>\d+)", data):
        furnitures.append(regex['furniture'])
        total_result += float(regex['price']) * int(regex['quantity'])

    data = input()

print("Bought furniture:")
if furnitures:
    print(*furnitures, sep='\n')
print(f"Total money spend: {total_result:.2f}")
