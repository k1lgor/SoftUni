l = input().split()
last_char = ''
for i in l:
    last_char = i
i = l.index(last_char)
print(' '.join(l[i:] + l[:i]))
