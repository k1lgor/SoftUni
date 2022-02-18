from collections import deque

fireworks = deque([int(x) for x in input().split(', ')])
exp_power = [int(x) for x in input().split(', ')]

storage = {
    'Palm Fireworks': 0,
    'Willow Fireworks': 0,
    'Crossette Fireworks': 0
}

while fireworks and exp_power:
    if fireworks[0] <= 0:
        fireworks.popleft()
        continue
    if exp_power[-1] <= 0:
        exp_power.pop()
        continue
    effect = fireworks.popleft()
    power = exp_power.pop()
    ttl = effect + power

    if not ttl % 3 and ttl % 5:
        storage['Palm Fireworks'] += 1
    elif not ttl % 5 and ttl % 3:
        storage['Willow Fireworks'] += 1
    elif not ttl % 3 and not ttl % 5:
        storage['Crossette Fireworks'] += 1
    else:
        fireworks.append(effect - 1)
        exp_power.append(power)

if storage['Palm Fireworks'] > 2 and storage['Willow Fireworks'] > 2 and storage['Crossette Fireworks'] > 2:
    print("Congrats! You made the perfect firework show!")
else:
    print("Sorry. You can't make the perfect firework show.")
if fireworks:
    print(f"Firework Effects left: {', '.join(str(x) for x in fireworks)}")
if exp_power:
    print(f"Explosive Power left: {', '.join(str(x) for x in exp_power)}")
for k, v in storage.items():
    print(f"{k}: {v}")
