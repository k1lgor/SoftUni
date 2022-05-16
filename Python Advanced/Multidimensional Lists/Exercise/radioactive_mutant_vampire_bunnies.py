import itertools


def player_pos(mtrx, x, y):
    for row, col in itertools.product(range(x), range(y)):
        if mtrx[row][col] == 'P':
            return [row, col]


# finding bunny position/s
def bunny_pos(mtrx, x, y, pos):
    pos = [[row, col] for row, col in itertools.product(
        range(x), range(y)) if mtrx[row][col] == 'B']

    return pos


# if the position (player/bunny) is inside the matrix
def inside(row, col, x, y):
    return 0 <= row < x and 0 <= col < y


# positions which bunny should spread
def bunny_spread_check(mtrx, x, y, pos, pos2):
    positions = []
    for p in pos:
        row, col = p[0], p[1]
        if inside(row - 1, col, x, y):
            positions.append([row - 1, col])
        if inside(row + 1, col, x, y):
            positions.append([row + 1, col])
        if inside(row, col + 1, x, y):
            positions.append([row, col + 1])
        if inside(row, col - 1, x, y):
            positions.append([row, col - 1])
    return positions


# spreading the bunny after player's movement
def bunny_spread(mtrx, positions):
    for pos in positions:
        row, col = pos[0], pos[1]
        if mtrx[row][col] in ['.', 'P']:
            mtrx[row][col] = 'B'
    return mtrx


# move up
def up(mtrx, x, y, pos):
    row, col = pos[0], pos[1]
    if inside(row - 1, col, x, y):
        return [row-1, col]
    return []


# move right
def right(mtrx, x, y, pos):
    row, col = pos[0], pos[1]
    if inside(row, col + 1, x, y):
        return [row, col + 1]
    return []


# move down
def down(mtrx, x, y, pos):
    row, col = pos[0], pos[1]
    if inside(row + 1, col, x, y):
        return [row + 1, col]
    return []


# move left
def left(mtrx, x, y, pos):
    row, col = pos[0], pos[1]
    if inside(row, col - 1, x, y):
        return [row, col - 1]
    return []


rows, cols = [int(x) for x in input().split()]
matrix = [list(input()) for _ in range(rows)]
commands = input()

bunny_positions = []
player_pos = player_pos(matrix, rows, cols)
bunny_pos = bunny_pos(matrix, rows, cols, bunny_positions)

out_of_lair = False
cought = False


for move in commands:
    last_player_pos = player_pos
    if move == 'U':
        player_pos = up(matrix, rows, cols, player_pos)
    elif move == 'R':
        player_pos = right(matrix, rows, cols, player_pos)
    elif move == 'D':
        player_pos = down(matrix, rows, cols, player_pos)
    elif move == 'L':
        player_pos = left(matrix, rows, cols, player_pos)

    if player_pos == []:
        matrix[last_player_pos[0]][last_player_pos[1]] = '.'
        out_of_lair = True
        bunny_pos = bunny_spread_check(
            matrix, rows, cols, bunny_pos, bunny_positions)
        bunny_positions = bunny_pos.copy()
        bunny_spread(matrix, bunny_positions)
        break
    else:
        if matrix[player_pos[0]][player_pos[1]] != 'B':
            matrix[player_pos[0]][player_pos[1]] = 'P'
        matrix[last_player_pos[0]][last_player_pos[1]] = '.'
        bunny_pos = bunny_spread_check(
            matrix, rows, cols, bunny_pos, bunny_positions)
        bunny_positions = bunny_pos.copy()
        bunny_spread(matrix, bunny_positions)
        if matrix[player_pos[0]][player_pos[1]] == 'B':
            cought = True
            break


if out_of_lair:
    for row in matrix:
        print(*row, sep='')
    print(f"won: {last_player_pos[0]} {last_player_pos[1]}")
if cought:
    for row in matrix:
        print(*row, sep='')
    print(f"dead: {player_pos[0]} {player_pos[1]}")
