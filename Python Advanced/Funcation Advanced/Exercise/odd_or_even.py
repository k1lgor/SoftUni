from functools import reduce


def multiply(command, data):
    if command == 'Odd':
        return reduce(lambda x, y: x + y, filter(lambda x: x %
                                                 2 == 1, data)) * len(data)
    else:
        return reduce(lambda x, y: x + y, filter(lambda x: x %
                                                 2 == 0, data)) * len(data)


print(multiply(input(), [int(x) for x in input().split()]))
