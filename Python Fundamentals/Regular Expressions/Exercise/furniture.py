import re

data = input()
furnitures = {}
result = 0

while data != "Purchase":
    regex = re.match(
        r">>(?P<furniture>[A-Za-z]+)<<(?P<price>\d+(\.\d+)?)\!(?P<quantity>\d+)", data)
    if regex:
        if regex['furniture'] not in furnitures:
            furnitures[regex['furniture']] = [
                float(regex['price']) * int(regex['quantity'])]
        else:
            furnitures[regex['furniture']].append(
                float(regex['price']) * int(regex['quantity']))

    data = input()

print("Bought furniture:")
for k, v in furnitures.items():
    for _ in range(len(v)):
        print(k)
for vv in furnitures.values():
    for vvv in vv:
        result += vvv
print(f"Total money spend: {result:.2f}")
