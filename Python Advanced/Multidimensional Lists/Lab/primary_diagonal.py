size = int(input())
matrix = [[int(x) for x in input().split()] for x in range(size)]

ttl_sum = sum(matrix[size - row - 1][size - row - 1] for row in range(size))
print(ttl_sum)
