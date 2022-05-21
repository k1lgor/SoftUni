import itertools
m = int(input())
counter = 0
if 4 <= m <= 144:
    for a, b, c, d in itertools.product(range(1, 10), range(1, 10), range(1, 10), range(1, 10)):
        if (a * b) + (c * d) == m and a < b and c > d:
            print(f'{a}{b}{c}{d}', end=' ')
            counter += 1
            if counter == 4:
                i = a
                j = b
                k = c
                l = d
print()
if counter >= 4:
    print(f'Password: {i}{j}{k}{l}')
else:
    print("No!")
