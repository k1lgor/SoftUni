l = input().split('|')
new = []

for i in l[::-1]:
    new += list(map(str, i.split()))
    
print(' '.join(new))
