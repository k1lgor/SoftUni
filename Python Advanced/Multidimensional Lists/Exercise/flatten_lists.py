data = input().split('|')
matrix = []

while data:
    for ele in data.pop().split():
        matrix.append(ele)
print(*matrix, sep=' ')
