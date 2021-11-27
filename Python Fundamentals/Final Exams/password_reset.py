data = input()
command = input()

while 'Done' not in command:
    command, *tokens = command.split()

    if command == 'TakeOdd':
        data = ''.join(d for i, d in enumerate(data) if i % 2 != 0)
        print(data)
    elif command == 'Cut':
        data = data.replace(
            data[int(tokens[0]):int(tokens[0]) + int(tokens[1])], "", 1)
        print(data)
    elif command == 'Substitute':
        if tokens[0] in data:
            data = data.replace(tokens[0], tokens[1])
            print(data)
        else:
            print("Nothing to replace!")
    command = input()

print(f"Your password is: {data}")
