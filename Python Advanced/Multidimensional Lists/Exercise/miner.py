import itertools


def start_pos(mtrx, sz):
    for row, col in itertools.product(range(sz), range(sz)):
        if mtrx[row][col] == 's':
            return [row, col]


def inside(row, col, sz):
    return 0 <= row < sz and 0 <= col < sz


def up(pos, sz):
    row, col = pos[0], pos[1]
    if inside(row - 1, col, sz):
        return [row - 1, col]


def right(pos, sz):
    row, col = pos[0], pos[1]
    if inside(row, col + 1, sz):
        return [row, col + 1]


def down(pos, sz):
    row, col = pos[0], pos[1]
    if inside(row + 1, col, sz):
        return [row + 1, col]


def left(pos, sz):
    row, col = pos[0], pos[1]
    if inside(row, col - 1, sz):
        return [row, col - 1]


def collected(mtrx, sz):
    return sum(mtrx[row][col] == 'c' for row, col in itertools.product(range(sz), range(sz)))


size = int(input())
commands = input().split()
matrix = [list(input().split()) for _ in range(size)]

start_pos = start_pos(matrix, size)
coal_collected = 0
end = False
for direction in commands:
    if direction == 'up':
        start_pos = up(start_pos, size)
        if start_pos is None:
            start_pos = last_pos
        elif matrix[start_pos[0]][start_pos[1]] == 'c':
            coal_collected += 1
            matrix[start_pos[0]][start_pos[1]] = '*'
        elif matrix[start_pos[0]][start_pos[1]] == 'e':
            end = True
            break
    elif direction == 'right':
        start_pos = right(start_pos, size)
        if start_pos is None:
            start_pos = last_pos
        elif matrix[start_pos[0]][start_pos[1]] == 'c':
            coal_collected += 1
            matrix[start_pos[0]][start_pos[1]] = '*'
        elif matrix[start_pos[0]][start_pos[1]] == 'e':
            end = True
            break
    elif direction == 'down':
        start_pos = down(start_pos, size)
        if start_pos is None:
            start_pos = last_pos
        elif matrix[start_pos[0]][start_pos[1]] == 'c':
            coal_collected += 1
            matrix[start_pos[0]][start_pos[1]] = '*'
        elif matrix[start_pos[0]][start_pos[1]] == 'e':
            end = True
            break
    elif direction == 'left':
        start_pos = left(start_pos, size)
        if start_pos is None:
            start_pos = last_pos
        elif matrix[start_pos[0]][start_pos[1]] == 'c':
            coal_collected += 1
            matrix[start_pos[0]][start_pos[1]] = '*'
        elif matrix[start_pos[0]][start_pos[1]] == 'e':
            end = True
            break
    last_pos = start_pos
if end:
    print(f"Game over! {start_pos[0], start_pos[1]}")
else:
    left_coal = collected(matrix, size)
    if left_coal == 0:
        print(f"You collected all coal! {start_pos[0], start_pos[1]}")
    else:
        print(f"{left_coal} pieces of coal left. {start_pos[0], start_pos[1]}")
