import math
x = int(input())
y = float(input())
z = int(input())
workers = int(input())

ttl_grape = x * y
wine = ttl_grape * 0.4 / 2.5
nl = '\n'

if wine >= z:
    wpp = abs(wine - z) / workers
    print(
        f'Good harvest this year! Total wine: {math.floor(wine):.0f} liters.{nl}{math.ceil(abs(wine - z)):.0f} liters left -> {math.ceil(wpp):.0f} liters per person.')
else:
    print(
        f'It will be a tough winter! More {math.floor(abs(wine -z)):.0f} liters wine needed.')
