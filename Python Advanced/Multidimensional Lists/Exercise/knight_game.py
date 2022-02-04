def knight(x, y, mtrx):
    return mtrx[x][y] == 'K'


def inside(x, y, size):
    return 0 <= x < size and 0 <= y < size


def attack_counter(x, y, mtrx):
    result = 0
    # row - 2, col - 1
    if inside(row - 2, col - 1, len(mtrx)) and knight(row - 2, col - 1, mtrx):
        result += 1
    # row - 2, col + 1
    if inside(row - 2, col + 1, len(mtrx)) and knight(row - 2, col + 1, mtrx):
        result += 1
    # row + 2, col - 1
    if inside(row + 2, col - 1, len(mtrx)) and knight(row + 2, col - 1, mtrx):
        result += 1
    # row + 2, col + 1
    if inside(row + 2, col + 1, len(mtrx)) and knight(row + 2, col + 1, mtrx):
        result += 1
    # row - 1, col + 2
    if inside(row - 1, col + 2, len(mtrx)) and knight(row - 1, col + 2, mtrx):
        result += 1
    # row - 1, col - 2
    if inside(row - 1, col - 2, len(mtrx)) and knight(row - 1, col - 2, mtrx):
        result += 1
    # row + 1, col - 2
    if inside(row + 1, col - 2, len(mtrx)) and knight(row + 1, col - 2, mtrx):
        result += 1
    # row + 1, col + 2
    if inside(row + 1, col + 2, len(mtrx)) and knight(row + 1, col + 2, mtrx):
        result += 1
    return result


size = int(input())
matrix = [list(input()) for _ in range(size)]

removed = 0

while True:
    table = {}

    for row in range(size):
        for col in range(size):
            if matrix[row][col] == '0':
                continue
            counter = attack_counter(row, col, matrix)
            if counter:
                table[(row, col)] = counter

    if len(table) == 0:
        break

    best_counter = 0
    knight_row, knight_col = 0, 0
    for coor, counter in table.items():
        if counter > best_counter:
            best_counter = counter
            knight_row, knight_col = coor[0], coor[1]

    matrix[knight_row][knight_col] = '0'
    removed += 1

print(removed)
