rows, cols = [int(x) for x in input().split(', ')]

matrix = []
for _ in range(rows):
    data = [int(x) for x in input().split(', ')]
    matrix.append(data)
ttl_sum = sum(sum(col) for col in matrix)
print(f"{ttl_sum}\n{matrix}")
