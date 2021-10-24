x1 = input()
x2 = input()
x3 = input()

counter = 0
counter1 = 0
counter2 = 0
counter3 = 0
for i in range(ord(x1), ord(x2) + 1):
    if i == ord(x3):
        continue
    counter1 += 1
    if counter1 == 3:
        break
    for j in range(ord(x1), ord(x2) + 1):
        if j == ord(x3):
            continue
        counter2 += 1
        if counter2 == 3:
            break
        for k in range(ord(x1), ord(x2) + 1):
            if k == ord(x3):
                continue
            counter3 += 1
            if counter3 == 3:
                break
            counter += 1
            counter1, counter2, counter3, = 0, 0, 0
            print(f'{chr(i)}{chr(j)}{chr(k)}', end=' ')
print(counter)
