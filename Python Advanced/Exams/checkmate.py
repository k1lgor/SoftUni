def king(m, s):
    for x in range(s):
        for y in range(s):
            if m[x][y] == 'K':
                return [x, y]


def up(m, x, y):
    while x > -1:
        if m[x][y] == 'Q':
            return [x, y]
        x -= 1


def right(m, x, y):
    while y < 8:
        if m[x][y] == 'Q':
            return [x, y]
        y += 1


def down(m, x, y):
    while x < 8:
        if m[x][y] == 'Q':
            return [x, y]
        x += 1


def left(m, x, y):
    while y > -1:
        if m[x][y] == 'Q':
            return [x, y]
        y -= 1


def top_left(m, x, y):
    while x > -1 and y > -1:
        if m[x][y] == 'Q':
            return [x, y]
        x -= 1
        y -= 1


def top_right(m, x, y):
    while y < 8 and x > -1:
        if m[x][y] == 'Q':
            return [x, y]
        y += 1
        x -= 1


def down_right(m, x, y):
    while x < 8 and y < 8:
        if m[x][y] == 'Q':
            return [x, y]
        x += 1
        y += 1


def down_left(m, x, y):
    while x < 8 and y > -1:
        if m[x][y] == 'Q':
            return [x, y]
        x += 1
        y -= 1


matrix = [list(input().split()) for _ in range(8)]
queens_pos = []

king_pos = king(matrix, 8)
directions = {
    'up': up,
    'down': down,
    'right': right,
    'left': left,
    'top_left': top_left,
    'top_right': top_right,
    'down_right': down_right,
    'down_left': down_left
}
for directions, step in directions.items():
    row, col = king_pos[0], king_pos[1]
    queens_pos.append(step(matrix, row, col))


while None in queens_pos:
    queens_pos.remove(None)
if queens_pos:
    for x in queens_pos:
        print(x)
else:
    print("The king is safe!")
