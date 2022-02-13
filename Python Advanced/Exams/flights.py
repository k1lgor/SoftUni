def flights(*args):
    storage = {}
    LIST = [str(x) for x in args]
    for x in LIST:
        if x == 'Finish':
            break
        if not x.isdigit():
            last_dest = x
            if x not in storage:
                storage[x] = 0
        else:
            storage[last_dest] += int(x)
    return storage


print(flights('Vienna', 256, 'Vienna', 26, 'Morocco',
      98, 'Paris', 115, 'Finish', 'Paris', 15))
print(flights('London', 0, 'New York', 9, 'Aberdeen', 215,
      'Sydney', 2, 'New York', 300, 'Nice', 0, 'Finish'))
print(flights('Finish', 'New York', 90, 'Aberdeen', 300, 'Sydney', 0))
