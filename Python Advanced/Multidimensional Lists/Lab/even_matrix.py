rows = int(input())

matrix = [[int(x) for x in input().split(', ')] for _ in range(rows)]

# for i in matrix:
#     for j in i[::-1]:
#         if j % 2 != 0:
#             i.remove(j)
even = [[x for x in row if x % 2 == 0] for row in matrix]
print(even)
