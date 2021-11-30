def add(c, tok0, tok1, tok2):
    if tok0 in c:
        print(f"{tok0} is already in the collection!")
    else:
        c[tok0] = {tok1: tok2}
        print(
            f"{tok0} by {tok1} in {tok2} added to the collection!")
    return c


def remove(c, tok0):
    if tok0 in c:
        del c[tok0]
        print(f"Successfully removed {tok0}!")
    else:
        print(
            f"Invalid operation! {tok0} does not exist in the collection.")
    return c


def change(c, tok0, tok1):
    if tok0 in c:
        key = list(c[tok0].keys())
        c[tok0][key[0]] = tok1
        print(f"Changed the key of {tok0} to {tok1}!")
    else:
        print(
            f"Invalid operation! {tok0} does not exist in the collection.")
    return c


number = int(input())
collection = {}

for _ in range(number):
    sonata = input().split("|")
    collection[sonata[0]] = {sonata[1]: sonata[2]}

command = input()

while 'Stop' not in command:
    action, *tokens = command.split("|")

    if action == 'Add':
        add(collection, tokens[0], tokens[1], tokens[2])

    elif action == 'Remove':
        remove(collection, tokens[0])

    elif action == 'ChangeKey':
        change(collection, tokens[0], tokens[1])

    command = input()

for k, v in sorted(collection.items()):
    for kk, vv in v.items():
        print(f"{k} -> Composer: {kk}, Key: {vv}")
