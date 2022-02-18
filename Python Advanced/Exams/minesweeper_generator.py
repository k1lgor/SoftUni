size = int(input())
bombs = int(input())

board = [[0 for i in range(size)] for j in range(size)]
mines = []
for mine in range(bombs):
    mines.append(eval(input()))

for mine in mines:
    x, y = mine
    board[x][y] = '*'
    neighbors = [(x-1, y), (x-1, y+1), (x, y-1), (x+1, y-1),
                 (x+1, y), (x+1, y+1), (x, y+1), (x-1, y-1)]
    for n in neighbors:
        if 0 <= n[0] <= size - 1 and 0 <= n[1] <= size - 1 and n not in mines:
            board[n[0]][n[1]] += 1
for x in board:
    print(*x)
