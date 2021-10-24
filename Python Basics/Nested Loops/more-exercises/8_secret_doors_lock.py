xxx = int(input())
xx = int(input())
x = int(input())

for i in range(1, xxx + 1):
    if i % 2 == 0:
        for j in range(1, xx + 1):
            if j in [2, 3, 5, 7]:
                for k in range(1, x + 1):
                    if k % 2 == 0:
                        print(i, j, k)
