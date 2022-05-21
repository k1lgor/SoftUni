import itertools
n = int(input())

for i, j, k, l in itertools.product(range(1, 10), range(1, 10), range(1, 10), range(1, 10)):
    if (
        i + j == k + l
        and n % (i + j) == 0
    ):
        print(f'{i}{j}{k}{l}', end=' ')
