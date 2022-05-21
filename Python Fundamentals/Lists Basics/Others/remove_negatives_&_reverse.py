l = list(map(int, input().split()))

for i in range(len(l) - 1, -1, -1):
    if l[i] < 0:
        l.remove(l[i])
l.reverse()
if not l:
    print('empty')
else:
    print(' '.join(str(i) for i in l))
