s = input().split()
p = int(input())
new = [int(num) * p for num in s]
l = [str(i) for i in new]
print(' '.join(l))
