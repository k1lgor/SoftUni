import itertools
one = int(input())
two = int(input())
five = int(input())
ttl = int(input())

if one >= 0 and two >= 0 and five >= 0 and ttl >= 0:
    for i, j, k in itertools.product(range(one + 1), range(two + 1), range(five + 1)):
        if (i * 1) + (j * 2) + (k * 5) == ttl:
            print(
                f'{i} * 1 lv. + {j} * 2 lv. + {k} * 5 lv. = {ttl} lv.')
