from math import floor
group = int(input())
days = int(input())

daily = 0
water = 0
food = 0
total = 0
daily = 50
for i in range(1, days + 1):
    if i % 15 == 0:
        group += 5
    if i % 10 == 0:
        group -= 2
    food = 2 * group
    total += daily - food
    if i % 5 == 0:
        total += 20 * group - 2 * group if i % 3 == 0 else 20 * group
    if i % 3 == 0:
        water = 3 * group
        total -= water

print(f'{group} companions received {floor(total / group)} coins each.')
