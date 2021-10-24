import math
budget = float(input())
statists = int(input())
cloth_person = float(input())

decor = budget * 0.1
cloth = cloth_person * statists
if statists >= 150:
    cloth *= 0.9

ttl = decor + cloth
if ttl > budget:
    print(
        f'Not enough money!\nWingard needs {abs(ttl - budget):.2f} leva more.')
else:
    print(
        f'Action!\nWingard starts filming with {abs(ttl - budget):.2f} leva left.')
