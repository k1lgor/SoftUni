import itertools


def player_pos(m, s):
    for x, y in itertools.product(range(s), range(s)):
        if m[x][y] == 'P':
            return [x, y]


def inside(x, y, s):
    return 0 <= x < s and 0 <= y < s


def up(x, y):
    return [x - 1, y]


def right(x, y):
    return [x, y + 1]


def down(x, y):
    return [x + 1, y]


def left(x, y):
    return [x, y - 1]


text = input()
size = int(input())
matrix = [list(input()) for _ in range(size)]
player_pos = player_pos(matrix, size)
turns = int(input())
outside = False
for _ in range(turns):
    turn = input()
    row, col = player_pos[0], player_pos[1]

    if turn == 'up':
        new_row, new_col = up(row, col)
        if new_row == -1:
            if text:
                text = text[:-1]
            outside = True

    elif turn == 'right':
        new_row, new_col = right(row, col)
        if new_col >= size:
            if text:
                text = text[:-1]
            outside = True

    elif turn == 'down':
        new_row, new_col = down(row, col)
        if new_row >= size:
            if text:
                text = text[:-1]
            outside = True

    elif turn == 'left':
        new_row, new_col = left(row, col)
        if new_col == -1:
            if text:
                text = text[:-1]
            outside = True

    if not outside:
        if matrix[new_row][new_col] != '-':
            text += matrix[new_row][new_col]
        matrix[row][col] = '-'
        matrix[new_row][new_col] = 'P'
        player_pos = [new_row, new_col]
    else:
        player_pos = [row, col]
        outside = False


print(text)
for x in matrix:
    print(*x, sep='')
