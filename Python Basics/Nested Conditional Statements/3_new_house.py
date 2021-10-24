type = input()
num = int(input())
budget = int(input())
sum = 0.0
if type == 'Roses':
    sum = num * 5
    if num > 80:
        sum = num * 5 * 0.9
elif type == 'Dahlias':
    sum = num * 3.8
    if num > 90:
        sum = num * 3.8 * 0.85
elif type == 'Tulips':
    sum = num * 2.8
    if num > 80:
        sum = num * 2.8 * 0.85
elif type == 'Narcissus':
    sum = num * 3
    if num < 120:
        sum = num * 3 * 1.15
elif type == 'Gladiolus':
    sum = num * 2.5
    if num < 80:
        sum = num * 2.5 * 1.2
if budget >= sum:
    print(
        f'Hey, you have a great garden with {num} {type} and {abs(budget - sum):.2f} leva left.')
else:
    print(f'Not enough money, you need {abs(budget - sum):.2f} leva more.')
