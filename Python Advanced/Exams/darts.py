def inside(x, y, sz):
    return 0 <= x < sz and 0 <= y < sz


def calculate(mtrx, x, y, sz):
    ttl = 0
    # for column
    for y in range(col, col + 1):
        for x in range(sz):
            if mtrx[x][y].isdigit():
                ttl += int(mtrx[x][y])
    # for row
    for x in range(row, row + 1):
        for y in range(sz):
            if mtrx[x][y].isdigit():
                ttl += int(mtrx[x][y])
    return ttl


size = 7
player1, player2 = input().split(', ')
matrix = [list(input().split()) for _ in range(7)]
coord = eval(input())
player1_points = 501
player2_points = 501
turn = 1
player1_throws = 0
player2_throws = 0
finish_player1 = False
finish_player2 = False
while coord:
    row, col = coord[0], coord[1]
    if turn % 2:
        player1_throws += 1
        if inside(row, col, size):
            if matrix[row][col].isdigit():
                player1_points -= int(matrix[row][col])
            if matrix[row][col] == 'D':
                player1_points -= calculate(matrix, row, col, size) * 2
            elif matrix[row][col] == 'T':
                player1_points -= calculate(matrix, row, col, size) * 3
            elif matrix[row][col] == 'B':
                finish_player1 = True
            if player1_points <= 0:
                print(f"{player1} won the game with {player1_throws} throws!")
                quit()
    if not turn % 2:
        player2_throws += 1
        if inside(row, col, size):
            if matrix[row][col].isdigit():
                player2_points -= int(matrix[row][col])
            if matrix[row][col] == 'D':
                player2_points -= calculate(matrix, row, col, size) * 2
            elif matrix[row][col] == 'T':
                player2_points -= calculate(matrix, row, col, size) * 3
            elif matrix[row][col] == 'B':
                finish_player2 = True
            if player2_points <= 0:
                print(f"{player2} won the game with {player2_throws} throws!")
                quit()
    if finish_player1:
        break
    if finish_player2:
        break
    turn += 1
    coord = eval(input())

if finish_player1:
    print(f"{player1} won the game with {player1_throws} throws!")
if finish_player2:
    print(f"{player2} won the game with {player2_throws} throws!")
