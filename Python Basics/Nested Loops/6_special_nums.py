n = int(input())
special = ''
for number in range(1111, 9999):
    string = str(number)
    counter = 0
    for i, d in enumerate(string):
        if int(d) == 0:
            break
        if n % int(d) == 0:
            counter += 1
            if counter == 4:
                print(number, end=' ')
