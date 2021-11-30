def rate(pl, ttl, p, r):
    if p not in pl:
        print("error")
    else:
        pl[p]['rating'] += float(r)
        ttl[p] += 1
    return pl, ttl


def update(pl, ttl, p, r):
    if p not in pl:
        print("error")
    else:
        pl[p]['rarity'] = int(r)
    return pl, ttl


def reset(pl, ttl, p):
    if p not in pl:
        print("error")
    else:
        pl[p]['rating'] = 0
        ttl[p] = 0
    return pl, ttl


number = int(input())
plants = {}
total_plants = {}

for _ in range(number):
    data = input().split("<->")
    plants[data[0]] = {'rarity': int(data[1]), 'rating': 0.00}
    total_plants[data[0]] = 0

command = input()

while 'Exhibition' not in command:
    action = command.split(": ")

    if action[0] == "Rate":
        plant, rating = action[1].split(" - ")
        rate(plants, total_plants, plant, rating)

    elif action[0] == "Update":
        plant, rarity = action[1].split(" - ")
        update(plants, total_plants, plant, rarity)

    elif action[0] == "Reset":
        plant = action[1]
        reset(plants, total_plants, plant)

    command = input()

for k, v in plants.items():
    for kk, vv in v.items():
        if kk == 'rarity' and plants[k]['rating'] != 0:
            plants[k]['rating'] = plants[k]['rating'] / total_plants[k]

print("Plants for the exhibition:")
for k, v in sorted(plants.items(), key=lambda kvp: (-kvp[1]['rarity'], -kvp[1]['rating'])):
    print(
        f"- {k}; Rarity: {v['rarity']}; Rating: {v['rating']:.2f}")
