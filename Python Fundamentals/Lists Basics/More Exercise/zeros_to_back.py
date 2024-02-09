string = input().split(', ')
zeros = []
new = []
for i in string:
    if (a := int(i)) == 0:
        zeros.append(a)
    else:
        new.append(a)
print(new + zeros)
