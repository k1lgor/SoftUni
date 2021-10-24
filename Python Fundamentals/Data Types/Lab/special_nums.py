n = int(input())

for i in range(1, n + 1):
    sum_of_digits = 0
    digits = str(i)
    for digit, index in enumerate(digits):
        sum_of_digits += int(index)
    if sum_of_digits == 5 or sum_of_digits == 7 or sum_of_digits == 11:
        print(f'{i} -> True')
    else:
        print(f'{i} -> False')
        