from collections import deque


toys = [int(x) for x in input().split()]
levels = deque(int(x) for x in input().split())

present = {
    "Doll": 150,
    "Wooden train": 250,
    "Teddy bear": 300,
    "Bicycle": 400
}
crafted = {}

while toys and levels:
    toy = toys.pop()
    level = levels.popleft()
    if toy == 0 and level == 0:
        continue
    if toy == 0:
        levels.appendleft(level)
    if level == 0:
        toys.append(toy)
    magic_level = toy * level
    if magic_level in present.values():
        for k, v in present.items():
            if v == magic_level:
                if k not in crafted:
                    crafted[k] = 1
                else:
                    crafted[k] += 1
                break
    elif magic_level > 0:
        toys.append(toy + 15)
    elif magic_level < 0:
        toys.append(toy + level)
if ("Doll" in crafted and "Wooden train" in crafted) or ("Teddy bear" in crafted and "Bicycle" in crafted):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")
if toys:
    print(f"Materials left: {', '.join(str(x) for x in reversed(toys))}")
if levels:
    print(f"Magic left: {', '.join(str(x) for x in levels)}")
for k, v in sorted(crafted.items()):
    print(f"{k}: {v}")
