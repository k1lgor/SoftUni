targets = list(map(lambda x: int(x), input().split()))
command = input().split()


def shoot(index, power):

    if 0 <= index < len(targets):
        targets[index] -= power
        if targets[index] <= 0:
            targets.pop(index)
    return targets


def add(index, value):

    if 0 <= index < len(targets):
        targets.insert(index, value)
    else:
        return print('Invalid placement!')
    return targets


def strike(index, radius):

    left = index - radius
    right = index + radius + 1
    if left < 0 or right > len(targets):
        return print("Strike missed!")
    for _ in range(left, right):
        targets.pop(left)
    return targets


while 'End' not in command:

    if 'Shoot' in command:
        shoot(int(command[1]), int(command[2]))
    elif 'Add' in command:
        add(int(command[1]), int(command[2]))
    elif 'Strike' in command:
        strike(int(command[1]), int(command[2]))

    command = input().split()
print('|'.join(str(n) for n in targets))
