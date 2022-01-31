size = int(input())
matrix = [[int(x) for x in input().split()] for x in range(size)]

sum_primary = 0
sum_secondary = 0

for i in range(size):
    sum_primary += matrix[i][i]
    sum_secondary += matrix[i][size - 1 - i]
print(f"{abs(sum_primary - sum_secondary)}")
