def rows(size, stars):
    for _ in range(size - stars):
        print(' ', end='')
    for _ in range(1, stars):
        print('*', end=' ')
    print('*')


size = int(input())

for stars in range(1, size):
    rows(size, stars)
for stars in range(size, 0, -1):
    rows(size, stars)
