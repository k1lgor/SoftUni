from math import sqrt
l = list(map(int, input().split()))
l.sort(reverse=True)
new = []
s = []
for i in l[::]:
    if i < 0:
        continue
    if sqrt(i) == int(sqrt(i)):
        new.append(i)
s = list(map(str, new))
print(' '.join(s))
