import itertools
for i, j in itertools.product(range(1, 11), range(1, 11)):
    print(f'{i} * {j} = {i * j}')
