import itertools
n1 = int(input())
n2 = int(input())

for i, j, k, l in itertools.product(range(n1, n2 + 1), range(n1, n2 + 1), range(n1, n2 + 1), range(n1, n2 + 1)):
    if (
        (j + k) % 2 == 0
        and i > l
        and (
            i % 2 == 0 and l % 2 != 0 or i % 2 != 0 and l % 2 == 0
        )
    ):
        print(f'{i}{j}{k}{l}', end=' ')
