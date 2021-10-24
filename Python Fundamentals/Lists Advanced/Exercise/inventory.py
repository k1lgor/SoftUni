items = list(map(str, input().split(', ')))
command = input().split(' - ')


def collect():

    if item not in items:
        items.append(item)
    return items


def drop():

    if item in items:
        items.remove(item)
    return items


def combine():

    if old in items:
        old_index = items.index(old)
        items.insert(old_index + 1, new)
    return items


def renew():

    if item in items:
        items.remove(item)
        items.append(item)
    return items


while 'Craft!' not in command:

    item = command[1]
    if 'Craft!' in command:
        break

    if 'Collect' in command:
        collect()
    elif 'Drop' in command:
        drop()
    elif 'Combine Items' in command:
        item = item.split(':')
        old = item[0]
        new = item[1]
        combine()
    elif 'Renew' in command:
        renew()

    command = input().split(' - ')

print(', '.join(items))
