shop_list = list(map(str, input().split("!")))
command = input()

while True:

    action, *item = command.split()

    if command == 'Go Shopping!':
        print(*shop_list, sep=', ')
        break

    if action == 'Urgent':
        for i in item:
            if i not in shop_list:
                shop_list.insert(0, i)

    elif action == 'Unnecessary':
        for i in item:
            if i in shop_list:
                index = shop_list.index(i)
                shop_list.pop(index)

    elif action == 'Correct':
        if item[0] in shop_list:
            index = shop_list.index(item[0])
            shop_list[index] = item[1]

    elif action == 'Rearrange':
        for i in item:
            if i in shop_list:
                index = shop_list.index(i)
                shop_list.append(shop_list.pop(index))

    command = input()
