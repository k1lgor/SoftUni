juniors = int(input())
seniors = int(input())
trace = input()
sum_total = 0.0

if trace == 'trail':
    sum_total = juniors * 5.5 + seniors * 7
elif trace == 'cross-country':
    sum_total = juniors * 8 + seniors * 9.5
    if juniors + seniors >= 50:
        sum_total *= 0.75
elif trace == 'downhill':
    sum_total = juniors * 12.25 + seniors * 13.75
elif trace == 'road':
    sum_total = juniors * 20 + seniors * 21.5

sum_total *= 0.95
print(f'{sum_total:.2f}')
