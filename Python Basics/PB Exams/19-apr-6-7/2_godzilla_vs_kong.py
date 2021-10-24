budget = float(input())
statists = int(input())
cloth = float(input())

decor = budget * 0.1
price_cloth = cloth * statists
if statists >= 150:
    price_cloth *= 0.9
budget -= decor + price_cloth
if budget < 0:
    print(f'Not enough money!\nWingard needs {abs(budget):.2f} leva more.')
else:
    print(f'Action!\nWingard starts filming with {abs(budget):.2f} leva left.')