rows, cols = [int(x) for x in input().split()]
matrix = [list(input().split()) for _ in range(rows)]
command = input()

while 'END' not in command:
    if command.startswith('swap') and len(command.split()) == 5:
        command = command.split()
        row1, col1, row2, col2 = int(command[1]), int(
            command[2]), int(command[3]), int(command[4])
        if (row1 < 0 or col1 < 0 or row2 < 0 or col2 < 0) or (row1 > rows or row2 > rows or col1 > cols or col2 > cols):
            print("Invalid input!")
        else:
            matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]
            for i in range(rows):
                for j in range(cols):
                    print(f"{matrix[i][j]}", end=' ')
                print()
    else:
        print("Invalid input!")
    command = input()
