def snake(m, s):
    for row in range(s):
        for col in range(s):
            if m[row][col] == 'S':
                return [row, col]


def lair(m, s):
    temp = []
    for row in range(s):
        for col in range(s):
            if m[row][col] == 'B':
                temp.append([row, col])
    return temp


def inside(x,  y, s):
    return 0 <= x < s and 0 <= y < s


def mtrx(m, sp):
    x, y = tuple(sp)
    m[x][y] = 'S'
    return m


def if_food(m, sp, s):
    if sp != []:
        x, y = sp[0], sp[1]
        if m[x][y] == '*':
            return 1
    return 0


def up(m, x, y, s, lp):
    if inside(x - 1, y, s):
        if m[x - 1][y] == 'B' and [x - 1, y] == lp[0]:
            return lp[1]
        elif m[x - 1][y] == 'B' and [x - 1, y] == lp[1]:
            return lp[0]
        return [x - 1, y]
    return []


def down(m, x, y, s, lp):
    if inside(x + 1, y, s):
        if m[x + 1][y] == 'B' and [x + 1, y] == lp[0]:
            return lp[1]
        elif m[x + 1][y] == 'B' and [x + 1, y] == lp[1]:
            return lp[0]
        return [x + 1, y]
    return []


def right(m, x, y, s, lp):
    if inside(x, y + 1, s):
        if m[x][y + 1] == 'B' and [x, y + 1] == lp[0]:
            return lp[1]
        elif m[x][y + 1] == 'B' and [x, y + 1] == lp[1]:
            return lp[0]
        return [x, y + 1]
    return []


def left(m, x, y, s, lp):
    if inside(x, y - 1, s):
        if m[x][y - 1] == 'B' and [x, y - 1] == lp[0]:
            return lp[1]
        elif m[x][y - 1] == 'B' and [x, y - 1] == lp[1]:
            return lp[0]
        return [x, y - 1]
    return []


size = int(input())
matrix = [[x for x in input()] for _ in range(size)]

snake_pos = snake(matrix, size)
lairs_pos = lair(matrix, size)

food = 0
out = False


while True:
    if food >= 10:
        break
    move = input()

    row, col = tuple(snake_pos)

    if move == 'up':
        snake_pos = up(matrix, row, col, size, lairs_pos)
        food += if_food(matrix, snake_pos, size)
    elif move == 'down':
        snake_pos = down(matrix, row, col, size, lairs_pos)
        food += if_food(matrix, snake_pos, size)
    elif move == 'right':
        snake_pos = right(matrix, row, col, size, lairs_pos)
        food += if_food(matrix, snake_pos, size)
    elif move == 'left':
        snake_pos = left(matrix, row, col, size, lairs_pos)
        food += if_food(matrix, snake_pos, size)
    if snake_pos == []:
        lair_count = 0
        out = True
        if lairs_pos:
            for i in lairs_pos:
                if matrix[i[0]][i[1]] == 'B':
                    lair_count += 1
            if lair_count != 2:
                matrix[lairs_pos[0][0]][lairs_pos[0][1]] = '.'
                matrix[lairs_pos[1][0]][lairs_pos[1][1]] = '.'
        matrix[row][col] = '.'
        break
    matrix[row][col] = '.'
    matrix = mtrx(matrix, snake_pos)


if out or food < 10:
    print('Game over!')
if food >= 10:
    print("You won! You fed the snake.")
print(f"Food eaten: {food}")
for x in matrix:
    print(*x, sep='')
