n = int(input())
comb = 0
for i in range(n + 1):
    for j in range(n + 1):
        for k in range(n + 1):
            if i + j + k == n:
                comb += 1
print(comb)
