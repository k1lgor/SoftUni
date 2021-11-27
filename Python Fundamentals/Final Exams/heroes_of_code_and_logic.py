number = int(input())
hero = {}

for _ in range(number):
    name, hp, mp = input().split()
    hero[name] = {'hp': int(hp), 'mp': int(mp)}

command = input()

while 'End' not in command:
    command, *tokens = command.split(" - ")

    if command == 'CastSpell':
        if hero[tokens[0]]['mp'] >= int(tokens[1]):
            hero[tokens[0]]['mp'] -= int(tokens[1])
            print(
                f"{tokens[0]} has successfully cast {tokens[2]} and now has {hero[tokens[0]]['mp']} MP!")
        else:
            print(f"{tokens[0]} does not have enough MP to cast {tokens[2]}!")
    elif command == 'TakeDamage':
        hero[tokens[0]]['hp'] -= int(tokens[1])
        if hero[tokens[0]]['hp'] > 0:
            print(
                f"{tokens[0]} was hit for {tokens[1]} HP by {tokens[2]} and now has {hero[tokens[0]]['hp']} HP left!")
        else:
            print(f"{tokens[0]} has been killed by {tokens[2]}!")
            del hero[tokens[0]]
    elif command == 'Recharge':
        hero[tokens[0]]['mp'] += int(tokens[1])
        if hero[tokens[0]]['mp'] < 200:
            recovered = int(tokens[1])
        else:
            recovered = 200 - hero[tokens[0]]['mp'] + int(tokens[1])
            hero[tokens[0]]['mp'] = 200
        print(f"{tokens[0]} recharged for {recovered} MP!")
    elif command == 'Heal':
        hero[tokens[0]]['hp'] += int(tokens[1])
        if hero[tokens[0]]['hp'] < 100:
            recovered = int(tokens[1])
        else:
            recovered = 100 - hero[tokens[0]]['hp'] + int(tokens[1])
            hero[tokens[0]]['hp'] = 100
        print(f"{tokens[0]} healed for {recovered} HP!")
    command = input()

for k, v in sorted(hero.items(), key=lambda x: (-x[1]['hp'], x[0])):
    print(f"{k}\n  HP: {v['hp']}\n  MP: {v['mp']}")
