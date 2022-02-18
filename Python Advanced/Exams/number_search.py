def numbers_searching(*args):
    unique = {}
    for x in args:
        if str(x) not in unique:
            unique[str(x)] = 0
        else:
            unique[str(x)] += 1
    missing = [x for x in range(min(args), max(args) + 1)]
    dublicates = [int(k) for k, v in unique.items() if v > 0]
    
    diff = list(set(missing).difference(set(args)))
    return [diff[0], sorted(dublicates)]


print(numbers_searching(1, 2, 4, 2, 5, 4))
print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))
print(numbers_searching(50, 50, 47, 47, 48,
      45, 49, 44, 47, 45, 44, 44, 48, 44, 48))
