msg = input()
command = input()

while 'Reveal' not in command:

    command, *tokens = command.split(":|:")

    if command == 'InsertSpace':
        msg = f"{msg[:int(tokens[0])]} {msg[int(tokens[0]):]}"
        print(msg)
    elif command == 'Reverse':
        if tokens[0] in msg:
            index = msg.find(tokens[0])
            cut = msg[index:index + len(tokens[0])]
            msg = msg[:index] + msg[index + len(tokens[0]):] + cut[::-1]
            print(msg)
        else:
            print('error')
    elif command == 'ChangeAll':
        msg = msg.replace(tokens[0], tokens[1])
        print(msg)

    command = input()

print(f"You have a new text message: {msg}")
