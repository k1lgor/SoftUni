cards = input().split(', ')
number = int(input())

for _ in range(number):
    action, *args = list(map(str, input().split(', ')))

    if action == 'Add':
        if args[0] not in cards[::]:
            cards.append(args[0])
            print("Card successfully added")
        else:
            print("Card is already in the deck")
    if action == 'Remove':
        if args[0] in cards[::]:
            cards.remove(args[0])
            print("Card successfully removed")
        else:
            print("Card not found")
    if action == 'Remove At':
        if 0 <= int(args[0]) < len(cards):
            cards.pop(int(args[0]))
            print("Card successfully removed")
        else:
            print("Index out of range")
    if action == 'Insert':
        if 0 <= int(args[0]) < len(cards):
            if args[1] not in cards[::]:
                cards.insert(int(args[0]), args[1])
                print("Card successfully added")
            else:
                print("Card is already added")
        else:
            print("Index out of range")

print(*cards, sep=', ')
