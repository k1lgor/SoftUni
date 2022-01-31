size = int(input())
matrix = [[int(x) for x in input().split(', ')] for x in range(size)]

primary = []
secondary = []

for i in range(size):
    primary.append(matrix[i][i])
    secondary.append(matrix[i][size - 1 - i])

print(f"Primary diagonal: {', '.join(str(x) for x in primary)}. Sum: {sum(primary)}")
print(f"Secondary diagonal: {', '.join(str(x) for x in secondary)}. Sum: {sum(secondary)}")
