import itertools


def bunny_pos(mtrx, sz):
    for row, col in itertools.product(range(size), range(size)):
        if mtrx[row][col] == 'B':
            return [row, col]


def up(row, col):
    return row - 1, col


def right(row, col):
    return row, col + 1


def down(row, col):
    return row + 1, col


def left(row, col):
    return row, col - 1


size = int(input())
matrix = [list(input().split()) for _ in range(size)]
bunny_pos = bunny_pos(matrix, size)
row, col = bunny_pos[0], bunny_pos[1]
directions = {
    'up': up,
    'down': down,
    'left': left,
    'right': right
}
max_sum = float('-inf')
max_direction = ''
max_coord = []
for direction, step in directions.items():
    row, col = bunny_pos[0], bunny_pos[1]
    ttl = 0
    coord = []
    while True:
        row, col = step(row, col)
        if row < 0 or col < 0 or row >= size or col >= size:
            break
        if matrix[row][col] == 'X':
            break
        coord.append([row, col])
        ttl += int(matrix[row][col])
    if ttl > max_sum and coord:
        max_sum = ttl
        max_direction = direction
        max_coord = coord
print(max_direction)
for x in max_coord:
    print(x)
print(max_sum)
