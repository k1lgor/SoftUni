data = input()
dwarves = {}
colors = {}
while data != 'Once upon a time':
    name, color, phys = data.split(" <:> ")
    phys = int(phys)
    ID = f"{name}:{color}"
    if ID not in dwarves:
        if color not in colors:
            colors[color] = 1
        else:
            colors[color] += 1
        dwarves[ID] = [0, color]
    dwarves[ID][0] = max(dwarves[ID][0], phys)
    data = input()

for k, v in sorted(dwarves.items(), key=lambda kvp: (kvp[1][0], colors[kvp[1][1]]), reverse=True):
    tokens = k.split(":")
    print(f"({tokens[1]}) {tokens[0]} <-> {v[0]}")
