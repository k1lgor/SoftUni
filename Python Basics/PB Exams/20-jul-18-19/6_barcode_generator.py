start = int(input())
end = int(input())

x1_start = start // 1000
x2_start = start // 100 % 10
x3_start = start // 10 % 10
x4_start = start % 10

x1_end = end // 1000
x2_end = end // 100 % 10
x3_end = end // 10 % 10
x4_end = end % 10

for i in range(x1_start, x1_end + 1):
    for j in range(x2_start, x2_end + 1):
        for k in range(x3_start, x3_end + 1):
            for l in range(x4_start, x4_end + 1):
                if i % 2 != 0 and j % 2 != 0 and k % 2 != 0 and l % 2 != 0:
                    print(f'{i}{j}{k}{l}', end=' ')
