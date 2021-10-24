wagons = [0] * int(input())

command = input()

while command != 'End':
        
    command = command.split()
    command1 = command[0]
    command2 = int(command[1])
    if len(command) > 2:
        command3 = int(command[2])

    if command1 == 'add':
        index = wagons[len(wagons) - 1] + command2
        wagons.pop(len(wagons) - 1)
        wagons.append(index)

    elif command1 == 'insert':
        index = wagons[command2] + command3
        wagons.pop(command2)
        wagons.insert(command2, index)

    elif command1 == 'leave':
        index = wagons[command2] - command3
        wagons.pop(command2)
        wagons.insert(command2, index)

    command = input()
print(wagons)
