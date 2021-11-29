def cast(h, tok0, tok1, tok2):
    if h[tok0]['mp'] >= int(tok1):
        h[tok0]['mp'] -= int(tok1)
        print(
            f"{tok0} has successfully cast {tok2} and now has {h[tok0]['mp']} MP!")
    else:
        print(f"{tok0} does not have enough MP to cast {tok2}!")
    return h


def damage(h, tok0, tok1, tok2):
    h[tok0]['hp'] -= int(tok1)
    if h[tok0]['hp'] > 0:
        print(
            f"{tok0} was hit for {tok1} HP by {tok2} and now has {h[tok0]['hp']} HP left!")
    else:
        print(f"{tok0} has been killed by {tok2}!")
        del h[tok0]
    return h


def recharge(h, tok0, tok1):
    h[tok0]['mp'] += int(tok1)
    if h[tok0]['mp'] < 200:
        recovered = int(tok1)
    else:
        recovered = 200 - h[tok0]['mp'] + int(tok1)
        h[tok0]['mp'] = 200
    print(f"{tok0} recharged for {recovered} MP!")
    return h


def heal(h, tok0, tok1):
    h[tok0]['hp'] += int(tok1)
    if h[tok0]['hp'] < 100:
        recovered = int(tok1)
    else:
        recovered = 100 - h[tok0]['hp'] + int(tok1)
        h[tok0]['hp'] = 100
    print(f"{tok0} healed for {recovered} HP!")
    return h


number = int(input())
hero = {}

for _ in range(number):
    name, hp, mp = input().split()
    hero[name] = {'hp': int(hp), 'mp': int(mp)}

command = input()

while 'End' not in command:
    command, *tokens = command.split(" - ")

    if command == 'CastSpell':
        cast(hero, tokens[0], tokens[1], tokens[2])

    elif command == 'TakeDamage':
        damage(hero, tokens[0], tokens[1], tokens[2])

    elif command == 'Recharge':
        recharge(hero, tokens[0], tokens[1])

    elif command == 'Heal':
        heal(hero, tokens[0], tokens[1])

    command = input()

for k, v in sorted(hero.items(), key=lambda x: (-x[1]['hp'], x[0])):
    print(f"{k}\n  HP: {v['hp']}\n  MP: {v['mp']}")
