import sys

rows, cols = [int(x) for x in input().split(', ')]

matrix = [[int(x) for x in input().split(', ')] for x in range(rows)]
max_sum = -sys.maxsize
max_submatrix = []
for row in range(rows - 1):
    for col in range(cols - 1):
        sub_matrix = [matrix[row][col], matrix[row][col + 1], matrix[row + 1][col], matrix[row + 1][col + 1]]

        if sum(sub_matrix) > max_sum:
            max_sum = sum(sub_matrix)
            max_submatrix = sub_matrix.copy()

print(max_submatrix[0], max_submatrix[1])
print(max_submatrix[2], max_submatrix[3])
print(max_sum)
