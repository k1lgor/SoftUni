def inside(row, col, sz):
    return 0 <= row < sz and 0 <= col < sz


def add(mtrx, row, col, n, sz):
    if inside(row, col, sz):
        mtrx[row][col] += int(n)
        return mtrx
    print("Invalid coordinates")


def subtract(mtrx, row, col, n, sz):
    if inside(row, col, sz):
        mtrx[row][col] -= int(n)
        return mtrx
    print("Invalid coordinates")


size = int(input())

matrix = [[int(x) for x in input().split()] for x in range(size)]
command = input()

while 'END' not in command:
    command, x, y, num = command.split()
    if command == 'Add':
        add(matrix, int(x), int(y), int(num), size)
    elif command == 'Subtract':
        subtract(matrix, int(x), int(y), int(num), size)
    command = input()

for row in matrix:
    print(*row)
