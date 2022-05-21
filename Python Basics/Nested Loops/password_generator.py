import itertools
n = int(input())
l = int(input())

for x1, x2, x3, x4 in itertools.product(range(1, n), range(1, n), range(97, 97 + l), range(97, 97 + l)):
    for x5 in range(1, n):
        if x5 > x1 and x5 > x2:
            print(f'{x1}{x2}{chr(x3)}{chr(x4)}{x5}', end=' ')
    print(f'{x1}{x2}{chr(x3)}{chr(x4)}{x5 + 1}', end=' ')
