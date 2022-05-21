import itertools
for i, j, k in itertools.product(range(24), range(60), range(60)):
    print(f'{i} : {j} : {k}')
