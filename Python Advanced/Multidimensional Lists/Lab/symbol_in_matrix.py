size = int(input())
matrix = [list(input().split()) for _ in range(size)]
symbol = input()

pos = 0
found = False
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        for k in range(len(matrix[i][j])):
            if matrix[i][j][k] == symbol:
                pos = (i, k)
                found = True
                break
    if found:
        break
if not found:
    print(f"{symbol} does not occur in the matrix")
else:
    print(pos)
