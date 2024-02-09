from collections import deque

effect = deque([int(x) for x in input().split(', ')])
casing = [int(x) for x in input().split(', ')]

materials = {
    'Datura Bombs': 0,
    'Cherry Bombs': 0,
    'Smoke Decoy Bombs': 0
}

while effect and casing and (materials['Datura Bombs'] <= 2 or materials['Cherry Bombs'] <= 2 or materials['Smoke Decoy Bombs'] <= 2):
    e = effect.popleft()
    c = casing.pop()

    if (ttl := e + c) == 40:
        materials['Datura Bombs'] += 1
    elif ttl == 60:
        materials['Cherry Bombs'] += 1
    elif ttl == 120:
        materials['Smoke Decoy Bombs'] += 1
    else:
        effect.appendleft(e)
        casing.append(c - 5)

if materials['Datura Bombs'] > 2 and materials['Cherry Bombs'] > 2 and materials['Smoke Decoy Bombs'] > 2:
    print("Bene! You have successfully filled the bomb pouch!")
else:
    print("You don't have enough materials to fill the bomb pouch.")
if effect:
    print(f"Bomb Effects: {', '.join(str(x) for x in effect)}")
else:
    print("Bomb Effects: empty")
if casing:
    print(f"Bomb Casings: {', '.join(str(x) for x in casing)}")
else:
    print("Bomb Casings: empty")
for k, v in sorted(materials.items()):
    print(f'{k}: {v}')
