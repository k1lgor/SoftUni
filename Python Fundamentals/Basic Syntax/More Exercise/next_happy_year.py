num = int(input()) + 1

while len(set(str(num))) != len(str(num)):
    num += 1
print(num)