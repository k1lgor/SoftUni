a1 = int(input())
a2 = int(input())
n = int(input())

for x1 in range(a1, a2):
    for x2 in range(1, n):
        for x3 in range(1, n // 2):
            x4 = chr(x1)
            if x1 % 2 != 0 and (x2 + x3 + x1) % 2 != 0:
                print(f'{chr(x1)}-{x2}{x3}{ord(x4)}')