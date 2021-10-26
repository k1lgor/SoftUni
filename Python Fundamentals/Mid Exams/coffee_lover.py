coffis, num = input().split(" "), int(input())

for _ in range(num):

    command, *args = input().split()

    if command == 'Include':
        coffis.append(args[0])
    if command == 'Remove' and 0 <= int(args[1]) < len(coffis):
        if args[0] == 'first':
            coffis = coffis[int(args[1]):]
        elif args[0] == 'last':
            coffis = coffis[:-int(args[1])]
    if (
        command == 'Prefer'
        and 0 <= int(args[0]) < len(coffis)
        and 0 <= int(args[1]) < len(coffis)
    ):
        temp = coffis[int(args[0])]
        coffis[int(args[0])] = coffis[int(args[1])]
        coffis[int(args[1])] = temp
    if command == 'Reverse':
        coffis.reverse()

print(f"Coffees:\n\n{' '.join(coffis)}")
