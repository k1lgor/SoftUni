import itertools
n = int(input())

for i, j, k in itertools.product(range(n), range(n), range(n)):
    print(f'{chr(97 + i)}{chr(97 + j)}{chr(97 + k)}')
