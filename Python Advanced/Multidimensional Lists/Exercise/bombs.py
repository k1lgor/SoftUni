def inside(x, y, size):
    return 0 <= x < size and 0 <= y < size


def around(x, y, mtrx):
    size = len(mtrx)
    around_matrix = []
    if inside(x - 1, y, size) and mtrx[x - 1][y] > 0:
        around_matrix.append([x - 1, y])
    if inside(x + 1, y, size) and mtrx[x + 1][y] > 0:
        around_matrix.append([x + 1, y])
    if inside(x, y - 1, size) and mtrx[x][y - 1] > 0:
        around_matrix.append([x, y - 1])
    if inside(x, y + 1, size) and mtrx[x][y + 1] > 0:
        around_matrix.append([x, y + 1])
    if inside(x + 1, y + 1, size) and mtrx[x + 1][y + 1] > 0:
        around_matrix.append([x + 1, y + 1])
    if inside(x - 1, y - 1, size) and mtrx[x - 1][y - 1] > 0:
        around_matrix.append([x - 1, y - 1])
    if inside(x + 1, y - 1, size) and mtrx[x + 1][y - 1] > 0:
        around_matrix.append([x + 1, y - 1])
    if inside(x - 1, y + 1, size) and mtrx[x - 1][y + 1] > 0:
        around_matrix.append([x - 1, y + 1])
    return around_matrix


size_matrix = int(input())
matrix = [[int(x) for x in input().split()] for x in range(size_matrix)]
bombs_coor = input().split()

for bomb in bombs_coor:
    bomb_x, bomb_y = [int(x) for x in bomb.split(',')]
    if matrix[bomb_x][bomb_y] <= 0:
        continue
    bomb_power = matrix[bomb_x][bomb_y]
    matrix[bomb_x][bomb_y] = 0

    for row, col in around(bomb_x, bomb_y, matrix):
        matrix[row][col] -= bomb_power

alive = 0
ttl_sum = 0
for row in matrix:
    for i in row:
        if i > 0:
            alive += 1
            ttl_sum += i
print(f"Alive cells: {alive}\nSum: {ttl_sum}")
for row in matrix:
    print(*row, sep=' ')
