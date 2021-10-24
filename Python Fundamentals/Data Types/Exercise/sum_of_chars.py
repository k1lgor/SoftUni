n = int(input())
sums = 0
for _ in range(1, n + 1):
    l = input()
    sums += ord(l)
print(f'The sum equals: {sums}')