number = int(input())
collection = {}

for _ in range(number):
    sonata = input().split("|")
    collection[sonata[0]] = {sonata[1]: sonata[2]}

command = input()

while 'Stop' not in command:
    action, *tokens = command.split("|")

    if action == 'Add':
        if tokens[0] in collection:
            print(f"{tokens[0]} is already in the collection!")
        else:
            collection[tokens[0]] = {tokens[1]: tokens[2]}
            print(
                f"{tokens[0]} by {tokens[1]} in {tokens[2]} added to the collection!")
    elif action == 'Remove':
        if tokens[0] in collection:
            del collection[tokens[0]]
            print(f"Successfully removed {tokens[0]}!")
        else:
            print(
                f"Invalid operation! {tokens[0]} does not exist in the collection.")
    elif action == 'ChangeKey':
        if tokens[0] in collection:
            key = list(collection[tokens[0]].keys())
            collection[tokens[0]][key[0]] = tokens[1]
            print(f"Changed the key of {tokens[0]} to {tokens[1]}!")
        else:
            print(
                f"Invalid operation! {tokens[0]} does not exist in the collection.")

    command = input()

for k, v in sorted(collection.items()):
    for kk, vv in v.items():
        print(f"{k} -> Composer: {kk}, Key: {vv}")
