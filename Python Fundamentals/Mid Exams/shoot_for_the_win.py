targets = [int(x) for x in input().split()]
index = input()
shot = 0

while 'End' not in index:

    if int(index) in range(len(targets)):

        value = targets[int(index)]

        for target in range(len(targets)):
            if targets[target] != -1:
                if targets[target] > value:
                    targets[target] -= value
                else:
                    targets[target] += value
        targets[int(index)] = -1
        shot += 1

    index = input()

print(f"Shot targets: {shot} -> {' '.join(map(str, targets))}")
