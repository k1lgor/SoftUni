n = int(input())
counter = 1
boolean = False
for row in range(1, n + 1):
    for _ in range(1, row + 1):
        if counter > n:
            boolean = True
            break
        print(f'{counter} ', end='')
        counter += 1
    if boolean:
        break
    print()
