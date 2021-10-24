x1 = int(input())
x2 = int(input())
x3 = int(input())

for i in range(2, x1 + 1, 2):
    for j in range(2, x2 + 1):
        for k in range(2, x3 + 1, 2):
            if j in [2, 3, 5, 7]:
                print(i, j, k)
