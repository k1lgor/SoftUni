def like(g, tok0, tok1):
    if tok0 not in g:
        g[tok0] = []
    if tok1 not in g[tok0]:
        g[tok0].append(tok1)
    return g


def unlike(g, tok0, tok1, un):
    if tok0 not in g:
        print(f"{tok0} is not at the party.")
    elif tok1 not in g[tok0]:
        print(f"{tok0} doesn't have the {tok1} in his/her collection.")
    else:
        g[tok0].remove(tok1)
        print(f"{tok0} doesn't like the {tok1}.")
        un.append(tok1)
    return g, un


command = input()
guest = {}
unliked = []

while 'Stop' not in command:
    command, *tokens = command.split("-")
    if command == 'Like':
        like(guest, tokens[0], tokens[1])
    elif command == 'Unlike':
        unlike(guest, tokens[0], tokens[1], unliked)

    command = input()

for k, v in sorted(guest.items(), key=lambda x: (-len(x[1]), x[0])):
    print(f"{k}: {', '.join(v)}")
print(f"Unliked meals: {len(unliked)}")
