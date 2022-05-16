rows, cols = list(map(int, input().split(', ')))

matrix = [list(map(int, input().split())) for _ in range(rows)]

for i in range(cols):
    col_sum = sum(matrix[j][i] for j in range(rows))
    print(col_sum)
