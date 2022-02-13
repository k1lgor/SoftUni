def even_odd(*args):
    if args[-1] == 'even':
        return [args[x] for x in range(len(args) - 1) if not args[x] % 2]
    else:
        return [args[x] for x in range(len(args) - 1) if args[x] % 2]


print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))
