num = int(input())

elements = set()

for _ in range(num):
    for x in input().split():
        elements.add(x)

[print(x) for x in elements]
