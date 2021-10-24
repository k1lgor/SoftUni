juniors = int(input())
seniors = int(input())
trace = input()
sum = 0.0

if trace == 'trail':
    sum = juniors * 5.5 + seniors * 7
elif trace == 'cross-country':
    sum = juniors * 8 + seniors * 9.5
    if juniors + seniors >= 50:
        sum *= 0.75
elif trace == 'downhill':
    sum = juniors * 12.25 + seniors * 13.75
elif trace == 'road':
    sum = juniors * 20 + seniors * 21.5

sum *= 0.95
print(f'{sum:.2f}')
