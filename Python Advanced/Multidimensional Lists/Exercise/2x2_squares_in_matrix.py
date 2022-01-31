rows, cols = [int(x) for x in input().split()]
matrix = [list(input().split()) for x in range(rows)]

counter = 0

for row in range(rows - 1):
    for col in range(cols - 1):
        submatrix = [matrix[row][col], matrix[row][col + 1], matrix[row + 1][col], matrix[row + 1][col + 1]]
        if submatrix[0] == submatrix[1] and submatrix[1] == submatrix[2] and submatrix[2] == submatrix[3] and \
                submatrix[3] == submatrix[0]:
            counter += 1
print(counter)
