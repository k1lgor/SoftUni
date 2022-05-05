def alice_pos(mtrx, sz):
    for row in range(sz):
        for col in range(sz):
            if mtrx[row][col] == 'A':
                return [row, col]


def inside(row, col, sz):
    return 0 <= row < size and 0 <= col < size


size = int(input())
matrix = [list(input().split()) for _ in range(size)]

alice_pos = alice_pos(matrix, size)

commands = input()
tea_bags = 0
outside_or_dead = True
while commands:
    row, col = alice_pos[0], alice_pos[1]
    matrix[row][col] = '*'
    if matrix[row][col] == 'R':
        matrix[row][col] == '*'
        break
    if tea_bags == 10:
        break

    if commands == 'up' and inside(row - 1, col, size):
        if matrix[row - 1][col].isdigit():
            tea_bags += int(matrix[row - 1][col])
            alice_pos = [row - 1, col]
        elif matrix[row - 1][col] in ['.', '*']:
            alice_pos = [row - 1, col]
        else:
            outside_or_dead = False

    elif commands == 'down' and inside(row + 1, col, size):
        if matrix[row + 1][col].isdigit():
            tea_bags += int(matrix[row + 1][col])
            alice_pos = [row + 1, col]
        elif matrix[row + 1][col] in ['.', '*']:
            alice_pos = [row + 1, col]
        else:
            outside_or_dead = False

    elif commands == 'right' and inside(row, col + 1, size):
        if matrix[row][col + 1].isdigit():
            tea_bags += int(matrix[row][col + 1])
            alice_pos = [row, col + 1]
        elif matrix[row][col + 1] in ['.', '*']:
            alice_pos = [row, col + 1]
        else:
            outside_or_dead = False

    elif commands == 'left' and inside(row, col - 1, size):
        if matrix[row][col - 1].isdigit():
            tea_bags += int(matrix[row][col - 1])
            alice_pos = [row, col - 1]
        elif matrix[row][col - 1] in ['.', '*']:
            alice_pos = [row, col - 1]
        else:
            outside_or_dead = False

    if not outside_or_dead:
        break
    commands = input()

if tea_bags == 10:
    print("She did it! She went to the tea party.")
if not outside_or_dead:
    print("Alice didn't make it to the tea party.")
print(' '.join(str(x) for x in matrix))
