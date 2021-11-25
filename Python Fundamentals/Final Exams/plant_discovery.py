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
        if plant not in plants:
            print("error")
        else:
            plants[plant]['rating'] += float(rating)
            total_plants[plant] += 1
    elif action[0] == "Update":
        plant, rarity = action[1].split(" - ")
        if plant not in plants:
            print("error")
        else:
            plants[plant]['rarity'] = int(rarity)
    elif action[0] == "Reset":
        plant = action[1]
        if plant not in plants:
            print("error")
        else:
            plants[plant]['rating'] = 0
            total_plants[plant] = 0
    command = input()

for k, v in plants.items():
    for kk, vv in v.items():
        if kk == 'rarity' and plants[k]['rating'] != 0:
            plants[k]['rating'] = plants[k]['rating'] / total_plants[k]

print("Plants for the exhibition:")
for k, v in sorted(plants.items(), key=lambda kvp: (-kvp[1]['rarity'], -kvp[1]['rating'])):
    print(
        f"- {k}; Rarity: {v['rarity']}; Rating: {v['rating']:.2f}")
