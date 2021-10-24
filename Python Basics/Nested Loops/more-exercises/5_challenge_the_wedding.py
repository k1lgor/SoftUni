men = int(input())
women = int(input())
tables = int(input())
ttl = men * women
counter = 0
while tables != 0:
    for man in range(1, men + 1):
        for woman in range(1, women + 1):
            if tables == 0 or counter == ttl:
                break
            print(f'({man} <-> {woman})', end=' ')
            tables -= 1
            counter += 1
    break
