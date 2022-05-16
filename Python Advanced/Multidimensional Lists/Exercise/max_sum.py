import itertools
import sys

rows, cols = [int(x) for x in input().split()]
matrix = [[int(x) for x in input().split()] for x in range(rows)]

sub_matrix = []
sum_sub_matrix = -sys.maxsize
max_sub_matrix = []
for row, col in itertools.product(range(rows - 2), range(cols - 2)):
    sub_matrix = [matrix[row][col], matrix[row][col + 1], matrix[row][col + 2],
                  matrix[row + 1][col], matrix[row +
                                               1][col + 1], matrix[row + 1][col + 2],
                  matrix[row + 2][col], matrix[row + 2][col + 1], matrix[row + 2][col + 2]]
    if sum(sub_matrix) > sum_sub_matrix:
        sum_sub_matrix = sum(sub_matrix)
        max_sub_matrix = sub_matrix.copy()
print(f"Sum = {sum_sub_matrix}")
print(f"{max_sub_matrix[0]} {max_sub_matrix[1]} {max_sub_matrix[2]}")
print(f"{max_sub_matrix[3]} {max_sub_matrix[4]} {max_sub_matrix[5]}")
print(f"{max_sub_matrix[6]} {max_sub_matrix[7]} {max_sub_matrix[8]}")
