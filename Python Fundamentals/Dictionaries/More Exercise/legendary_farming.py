item_list = input()
key_items = {'shards': 0, 'fragments': 0, 'motes': 0}
legendary_items = {'shards': 'Shadowmourne', 'fragments': 'Valanyr', 'motes': 'Dragonwrath'}
junk_items = {}
is_obtained = False

while not is_obtained:
    split_items = item_list.split()

    for index in range(0, len(split_items), 2):
        if is_obtained:
            break
        material = split_items[index + 1].lower()
        quantity = split_items[index]
        if material in key_items:
            key_items[material] += int(quantity)
        else:
            if material not in junk_items:
                junk_items[material] = 0
            junk_items[material] += int(quantity)

        for k, v in key_items.items():
            if v >= 250:
                key_items[k] -= 250
                is_obtained = True
                print(f"{legendary_items[k]} obtained!")
                break
    if is_obtained:
        break
    item_list = input()

sort_key_items = sorted(key_items.items(), key=lambda kvp: (-kvp[1], kvp[0]))
for k, v in sort_key_items:
    print(f"{k}: {v}")
sort_junk_items = sorted(junk_items.items(), key=lambda kvp: kvp[0])
for k, v in sort_junk_items:
    print(f"{k}: {v}")
