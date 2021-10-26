phones = input().split(", ")

while True:

    action = input().split(' - ')

    if action[0] == 'End':
        break
    if action[0] == 'Add' and action[1] not in phones:
        phones.append(action[1])
    if action[0] == 'Remove':
        while action[1] in phones:
            phones.remove(action[1])
    if action[0] == 'Bonus phone':
        phone1, phone2 = action[1].split(':')
        if phone1 in phones:
            phones.insert(phones.index(phone1) + 1, phone2)
    if action[0] == 'Last' and action[1] in phones:
        phones.append(phones.pop(phones.index(action[1])))

print(*phones, sep=', ')
