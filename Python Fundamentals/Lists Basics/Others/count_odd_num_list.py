l = list(map(int, input().split()))
counter = sum(i % 2 != 0 for i in l)
print(counter)
