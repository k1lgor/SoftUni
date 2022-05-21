type_of = input()
num = int(input())
budget = int(input())
sum_total = 0.0
if type_of == 'Dahlias':
    sum_total = num * 3.8 * 0.85 if num > 90 else num * 3.8
elif type_of == 'Gladiolus':
    sum_total = num * 2.5 * 1.2 if num < 80 else num * 2.5
elif type_of == 'Narcissus':
    sum_total = num * 3 * 1.15 if num < 120 else num * 3
elif type_of == 'Roses':
    sum_total = num * 5 * 0.9 if num > 80 else num * 5
elif type_of == 'Tulips':
    sum_total = num * 2.8 * 0.85 if num > 80 else num * 2.8
if budget >= sum_total:
    print(
        f'Hey, you have a great garden with {num} {type_of} and {abs(budget - sum_total):.2f} leva left.')
else:
    print(
        f'Not enough money, you need {abs(budget - sum_total):.2f} leva more.')
