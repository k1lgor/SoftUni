def dic_add(cur_pirates, cur_city, cur_pop, cur_gold):
    if cur_city not in cur_pirates:
        cur_pirates[cur_city] = {'pop': int(cur_pop), 'gold': int(cur_gold)}
    else:
        cur_pirates[cur_city]['pop'] += int(cur_pop)
        cur_pirates[cur_city]['gold'] += int(cur_gold)
    return cur_pirates


def plunder(cur_pirates, tok0, tok1, tok2):
    cur_pirates[tok0]['pop'] -= int(tok1)
    cur_pirates[tok0]['gold'] -= int(tok2)
    print(
        f"{tok0} plundered! {tok2} gold stolen, {tok1} citizens killed.")
    if cur_pirates[tok0]['pop'] <= 0 or cur_pirates[tok0]['gold'] <= 0:
        del cur_pirates[tok0]
        print(f"{tok0} has been wiped off the map!")
    return cur_pirates


def prosper(cur_pirates, tok0, tok1):
    if int(tok1) < 0:
        print("Gold added cannot be a negative number!")
    else:
        cur_pirates[tok0]['gold'] += int(tok1)
        print(
            f"{int(tok1)} gold added to the city treasury. {tok0} now has {cur_pirates[tok0]['gold']} gold.")
    return cur_pirates


def if_pirates(cur_pirates):
    if not cur_pirates:
        print("Ahoy, Captain! All targets have been plundered and destroyed!")
    else:
        print(
            f"Ahoy, Captain! There are {len(cur_pirates.keys())} wealthy settlements to go to:")
        for k, v in sorted(cur_pirates.items(), key=lambda x: (-x[1]['gold'], x[0])):
            print(
                f"{k} -> Population: {v['pop']} citizens, Gold: {v['gold']} kg")


command = input()
pirates = {}

while 'Sail' not in command:
    city, population, gold = command.split("||")

    dic_add(pirates, city, population, gold)

    command = input()

command = input()

while 'End' not in command:
    command, *tokens = command.split("=>")

    if command == 'Plunder':
        plunder(pirates, tokens[0], tokens[1], tokens[2])
    elif command == 'Prosper':
        prosper(pirates, tokens[0], tokens[1])

    command = input()

if_pirates(pirates)
