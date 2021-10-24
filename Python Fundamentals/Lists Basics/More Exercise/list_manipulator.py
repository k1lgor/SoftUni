import sys

initial = list(map(int, input().split()))
command = input()
while command != 'end':
    
    command_split = command.split()
    command1 = command_split[0]
    command2 = command_split[1]
    if len(command_split) > 2:
        command3 = command_split[2]

    if command1 == 'exchange':
        if (int(command2) > len(initial)) or (int(command2) < 0):
            print('Invalid index')
        else:
            initial = initial[int(command2) + 1:] + initial[:int(command2) + 1]
    elif command1 == 'max':
        max_value = 0
        index = 0
        if command2 == 'odd':
            for i, d in enumerate(initial):
                if d > max_value and d % 2 != 0:
                    max_value = d
                    index = i
            if index == 0 and max_value == 0:
                print('No matches')
            else:
                print(index)
        elif command2 == 'even':
            for i, d in enumerate(initial):
                if d > max_value and d % 2 == 0:
                    max_value = d
                    index = i
            if index == 0 and max_value == 0:
                print('No matches')
            else:
                print(index)
    elif command1 == 'min':
        min_value = sys.maxsize
        index = 0
        if command2 == 'odd':
            for i, d in enumerate(initial):
                if d < min_value and d % 2 != 0:
                    min_valie = d
                    index = i
            if index == 0 and min_value == sys_maxsize:
                print('No matches')
            else:
                print(index)
        elif command2 == 'even':
            for i, d in enumerate(initial):
                if d < min_value and d % 2 == 0:
                    min_value = d
                    index = i
            if index == 0 and min_value == sys.maxsize:
                print('No matches')
            else:
                print(index)
    elif command1 == 'first':
        List = []
        counter = 0
        if (
            command3 == 'odd'
            and int(command2) > len(initial)
            or command3 != 'odd'
            and command3 == 'even'
            and int(command2) > len(initial)
        ):
            print('Invalid count')
        elif command3 == 'odd':
            for count in initial:
                if counter == int(command2):
                    break
                if count % 2 != 0:
                    counter += 1
                    List.append(count)
            print(List)
        elif command3 == 'even':
            for count in initial:
                if counter == int(command2):
                    break
                if count % 2 == 0:
                    counter += 1
                    List.append(count)
            print(List)
    elif command1 == 'last':
        List = []
        counter = 0

        if (
            command3 == 'odd'
            and int(command2) > len(initial)
            or command3 != 'odd'
            and command3 == 'even'
            and int(command2) > len(initial)
        ):
            print('Invalid count')
        elif command3 == 'odd':
            for count in initial[::-1]:
                if counter == int(command2):
                    break
                if count % 2 != 0:
                    counter += 1
                    List.append(count)
            print(List)
        elif command3 == 'even':
            for count in initial[::-1]:
                if counter == int(command2):
                    break
                if count % 2 == 0:
                    counter += 1
                    List.append(count)
            print(List)
    command = input()
print(initial)