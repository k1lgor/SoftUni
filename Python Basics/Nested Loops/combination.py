import itertools
n = int(input())
comb = sum(i + j + k == n for i, j,
           k in itertools.product(range(n + 1), range(n + 1), range(n + 1)))

print(comb)
