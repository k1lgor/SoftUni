qnty = int(input())
days = int(input())

spirit = 0
cost = 0

for day in range(1, days + 1):
    if day % 11 == 0:
        qnty += 2
    if day % 2 == 0:
        cost += qnty * 2
        spirit += 5
    if day % 3 == 0:
        cost += qnty * 5 + qnty * 3
        spirit += 13
    if day % 5 == 0:
        cost += qnty * 15
        spirit += 17
        if day % 3 == 0:
            spirit += 30
    if day % 10 == 0:
        spirit -= 20
        cost += 5 + 3 + 15
        if day == days:
            spirit -= 30

print(f'Total cost: {cost:.0f}\nTotal spirit: {spirit}')
