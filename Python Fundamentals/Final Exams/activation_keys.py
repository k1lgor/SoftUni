data = input()
command = input()

while 'Generate' not in command:
    command, *tokens = command.split(">>>")

    if command == "Contains":
        if tokens[0] in data:
            print(f"{data} contains {tokens[0]}")
        else:
            print("Substring not found!")
    elif command == "Flip" and tokens[0] == "Upper":
        start = data[:int(tokens[1])]
        sub = data[int(tokens[1]):int(tokens[2])]
        mid = ''.join(i.upper() for i in sub)
        end = data[int(tokens[2]):]
        data = start + mid + end
        print(data)
    elif command == "Flip" and tokens[0] == "Lower":
        start = data[:int(tokens[1])]
        sub = data[int(tokens[1]):int(tokens[2])]
        mid = ''.join(i.lower() for i in sub)
        end = data[int(tokens[2]):]
        data = start + mid + end
        print(data)
    elif command == "Slice":
        data = data[:int(tokens[0])] + data[int(tokens[1]):]
        print(data)

    command = input()

print(f"Your activation key is: {data}")
