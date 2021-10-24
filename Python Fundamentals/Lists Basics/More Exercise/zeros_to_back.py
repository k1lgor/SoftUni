string = input().split(', ')
zeros = []
new = []
for i in string:
    a = int(i)
    if a == 0:
        zeros.append(a)
    else:
        new.append(a)
print(new + zeros)