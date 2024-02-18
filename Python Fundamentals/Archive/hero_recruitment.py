def enroll(h, tok0):
    if tok0 not in h:
        h[tok0] = []
    else:
        print(f"{tok0} is already enrolled.")
    return h


def learn(h, tok0, tok1):
    if tok0 not in h:
        print(f"{tok0} doesn't exist.")
    elif tok1 in h[tok0]:
        print(f"{tok0} has already learnt {tok1}.")
    else:
        h[tok0].append(tok1)
    return h


def unlearn(h, tok0, tok1):
    if tok0 not in h:
        print(f"{tok0} doesn't exist.")
    elif tok1 not in h[tok0]:
        print(f"{tok0} doesn't know {tok1}")
    else:
        h[tok0].remove(tok1)
    return h


command = input()
hero = {}
while "End" not in command:
    command, *tokens = command.split()

    if command == "Enroll":
        enroll(hero, tokens[0])
    elif command == "Learn":
        learn(hero, tokens[0], tokens[1])
    elif command == "Unlearn":
        unlearn(hero, tokens[0], tokens[1])

    command = input()

print("Heroes:")
for k, v in sorted(hero.items(), key=lambda x: (-len(x[1]), x[0])):
    print(f"== {k}: {', '.join(v)}")
