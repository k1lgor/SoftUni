encrypted = input()
command = input()

while 'Decode' not in command:

    command, *tokens = command.split("|")
    if command == "Move":
        encrypted = encrypted[int(tokens[0]):] + encrypted[:int(tokens[0])]
    elif command == "Insert":
        encrypted = encrypted[:int(tokens[0])] + \
            tokens[1] + encrypted[int(tokens[0]):]
    elif command == "ChangeAll":
        encrypted = encrypted.replace(tokens[0], tokens[1])

    command = input()

print(f"The decrypted message is: {encrypted}")
