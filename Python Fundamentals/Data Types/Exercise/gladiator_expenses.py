lost_fights = int(input())
helmet = float(input())
sword = float(input())
shield = float(input())
armor = float(input())

cost = 0
shield_break = 0
for i in range(1, lost_fights + 1):
    if i % 2 == 0:
        cost += helmet
    if i % 3 == 0:
        cost += sword
    if i % 2 == 0 and i % 3 == 0:
        cost += shield
        shield_break += 1
        if shield_break % 2 == 0:
            cost += armor
print(f'Gladiator expenses: {cost:.2f} aureus')