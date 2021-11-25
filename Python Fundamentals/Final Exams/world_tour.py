stops = input()
command = input()

while 'Travel' not in command:
    command, *tokens = command.split(":")

    if command == "Add Stop":
        if 0 <= int(tokens[0]) < len(stops):
            stops = stops[:int(tokens[0])] + tokens[1] + stops[int(tokens[0]):]
        print(stops)
    elif command == "Remove Stop":
        if 0 <= int(tokens[0]) < len(stops) and 0 <= int(tokens[1]) < len(stops):
            stops = stops[:int(tokens[0])] + stops[int(tokens[1]) + 1:]
        print(stops)
    elif command == "Switch":
        if tokens[0] in stops:
            stops = stops.replace(tokens[0], tokens[1])
        print(stops)
    command = input()

print(f"Ready for world tour! Planned stops: {stops}")
