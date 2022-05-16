from math import factorial


def get_magic_triangle(n):
    triangle = []
    for i in range(n):
        temp = [factorial(i) // (factorial(j) * factorial(i - j))
                for j in range(i+1)]
        triangle.append(temp)
    return triangle


# def get_magic_triangle(n):
#     triangle = []
#     if not n <= 0:
#         for x in range(n):
#             triangle.append([])
#         for i in range(1, n + 1):
#             m = 1
#             for j in range(1, i + 1):
#                 triangle[i - 1].append(m)
#                 m = (m * (i - j) // j)
#         if len(triangle) == 1:
#             return [1]
#         return triangle

get_magic_triangle(10)
