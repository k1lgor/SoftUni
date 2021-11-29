command = input()
pirates = {}

while 'Sail' not in command:
    city, population, gold = command.split("||")
    if city not in pirates:
        pirates[city] = {'pop': int(population), 'gold': int(gold)}
    else:
        pirates[city]['pop'] += int(population)
        pirates[city]['gold'] += int(gold)

    command = input()

command = input()

while 'End' not in command:
    command, *tokens = command.split("=>")

    if command == 'Plunder':
        pirates[tokens[0]]['pop'] -= int(tokens[1])
        pirates[tokens[0]]['gold'] -= int(tokens[2])
        print(
            f"{tokens[0]} plundered! {tokens[2]} gold stolen, {tokens[1]} citizens killed.")
        if pirates[tokens[0]]['pop'] <= 0 or pirates[tokens[0]]['gold'] <= 0:
            del pirates[tokens[0]]
            print(f"{tokens[0]} has been wiped off the map!")
    elif command == 'Prosper':
        if int(tokens[1]) < 0:
            print("Gold added cannot be a negative number!")
        else:
            pirates[tokens[0]]['gold'] += int(tokens[1])
            print(
                f"{int(tokens[1])} gold added to the city treasury. {tokens[0]} now has {pirates[tokens[0]]['gold']} gold.")

    command = input()

if not pirates:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")
else:
    print(
        f"Ahoy, Captain! There are {len(pirates.keys())} wealthy settlements to go to:")
    for k, v in sorted(pirates.items(), key=lambda x: (-x[1]['gold'], x[0])):
        print(f"{k} -> Population: {v['pop']} citizens, Gold: {v['gold']} kg")
