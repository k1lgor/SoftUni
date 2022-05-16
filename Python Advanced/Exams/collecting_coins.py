import itertools
import math


def player_pos(m, s):
    for row, col in itertools.product(range(s), range(s)):
        if m[row][col] == 'P':
            return [row, col]


def up(x, y):
    return x - 1, y


def right(x, y):
    return x, y + 1


def down(x, y):
    return x + 1, y


def left(x, y):
    return x, y - 1


def inside(x, y, s):
    return 0 <= x < s and 0 <= y < s


size = int(input())
matrix = [list(input().split()) for _ in range(size)]
coins = 0

player_pos = player_pos(matrix, size)
path = [[player_pos[0], player_pos[1]]]
loss = False
while True:
    if coins >= 100:
        break
    direction = input()

    if direction in ['up', 'right', 'down', 'left']:
        curr_row, curr_col = player_pos[0], player_pos[1]
        if direction == 'up':
            curr_row, curr_col = up(curr_row, curr_col)
            if curr_row == -1:
                curr_row = size - 1
        elif direction == 'right':
            curr_row, curr_col = right(curr_row, curr_col)
            if curr_col >= size:
                curr_col -= size
        elif direction == 'down':
            curr_row, curr_col = down(curr_row, curr_col)
            if curr_row >= size:
                curr_row -= size
        elif direction == 'left':
            curr_row, curr_col = left(curr_row, curr_col)
            if curr_col == -1:
                curr_col = size - 1

        if matrix[curr_row][curr_col].isdigit():
            coins += int(matrix[curr_row][curr_col])
            matrix[curr_row][curr_col] = '.'
        if matrix[curr_row][curr_col] == 'X':
            coins = math.floor(coins / 2)
            path.append([curr_row, curr_col])
            loss = True
            break
        path.append([curr_row, curr_col])
        player_pos = [curr_row, curr_col]
if not loss:
    print(f"You won! You've collected {coins} coins.")
else:
    print(f"Game over! You've collected {coins} coins.")
print("Your path:")
for item in path:
    print(item)
