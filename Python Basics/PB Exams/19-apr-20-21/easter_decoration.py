clients = int(input())
ttl = 0
for _ in range(clients):
    command = ''
    counter = 0
    price = 0
    while command != 'Finish':
        if (command := input()) == 'Finish':
            if counter % 2 == 0:
                price *= 0.8
            print(f'You purchased {counter} items for {price:.2f} leva.')
            break
        if command == 'basket':
            counter += 1
            price += 1.5
        elif command == 'chocolate bunny':
            counter += 1
            price += 7
        elif command == 'wreath':
            counter += 1
            price += 3.8
    ttl += price
print(f'Average bill per client is: {(ttl / clients):.2f} leva.')
