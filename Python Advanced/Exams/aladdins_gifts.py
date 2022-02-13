from collections import deque

materials = [int(x) for x in input().split()]
magic_level = deque([int(x) for x in input().split()])
presents = {}

while materials and magic_level:

    num_materials = materials.pop()
    num_magic_level = magic_level.popleft()
    ttl = num_magic_level + num_materials
    if ttl < 100:
        if not ttl % 2:
            num_materials *= 2
            num_magic_level *= 3
            ttl = num_magic_level + num_materials
        else:
            ttl *= 2
    if ttl > 499:
        ttl /= 2
    if 100 <= ttl <= 199:
        if 'Gemstone' not in presents:
            presents['Gemstone'] = 0
        presents['Gemstone'] += 1
    elif 200 <= ttl <= 299:
        if 'Porcelain Sculpture' not in presents:
            presents['Porcelain Sculpture'] = 0
        presents['Porcelain Sculpture'] += 1
    elif 300 <= ttl <= 399:
        if 'Gold' not in presents:
            presents['Gold'] = 0
        presents['Gold'] += 1
    elif 400 <= ttl <= 499:
        if 'Diamond Jewellery' not in presents:
            presents['Diamond Jewellery'] = 0
        presents['Diamond Jewellery'] += 1
if ('Gemstone' in presents and 'Porcelain Sculpture' in presents) or ('Gold' in presents and 'Diamond Jewellery' in presents):
    print("The wedding presents are made!")
else:
    print("Aladdin does not have enough wedding presents.")
if materials:
    print(f"Materials left: {', '.join(str(x) for x in materials)}")
if magic_level:
    print(f"Magic left: {', '.join(str(x) for x in magic_level)}")
if presents:
    for k, v in sorted(presents.items(), key=lambda x: x[0]):
        print(f"{k}: {v}")
