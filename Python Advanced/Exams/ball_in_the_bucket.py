def coordinates(d):
    num = ''
    coor = []
    for char in d:
        if char.isdigit():
            num += char
        if char == ',':
            coor.append(int(num))
            num = ''
    coor.append(int(num))
    return coor


def inside(x, y, sz):
    return 0 <= x < sz and 0 <= y < sz


def calculate(mtrx, row, col, sz):
    ttl = 0
    for y in range(col, col + 1):
        for x in range(sz):
            if mtrx[x][y].isdigit():
                ttl += int(mtrx[x][y])
    return ttl


size = 6
matrix = [list(input().split()) for _ in range(size)]
points = 0
min_points = 100

for _ in range(3):
    data = list(input())
    coord = coordinates(data)
    curr_row, curr_col = coord[0], coord[1]
    if inside(curr_row, curr_col, size) and matrix[curr_row][curr_col] == 0:
        continue
    if not inside(curr_row, curr_col, size):
        continue
    if inside(curr_row, curr_col, size) and matrix[curr_row][curr_col] == 'B':
        points += calculate(matrix, curr_row, curr_col, size)
        matrix[curr_row][curr_col] = 0

if points < min_points:
    print(f"Sorry! You need {min_points - points} points more to win a prize.")
else:
    if 100 <= points <= 199:
        print(
            f"Good job! You scored {points} points, and you've won Football.")
    elif 200 <= points <= 299:
        print(
            f"Good job! You scored {points} points, and you've won Teddy Bear.")
    elif points >= 300:
        print(
            f"Good job! You scored {points} points, and you've won Lego Construction Set.")
