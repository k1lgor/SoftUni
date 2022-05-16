data = input().split('|')
matrix = []

while data:
    matrix.extend(iter(data.pop().split()))
print(*matrix, sep=' ')
