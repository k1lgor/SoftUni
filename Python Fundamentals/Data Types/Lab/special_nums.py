n = int(input())

for i in range(1, n + 1):
    digits = str(i)
    sum_of_digits = sum(int(index) for index in digits)
    if sum_of_digits in [5, 7, 11]:
        print(f'{i} -> True')
    else:
        print(f'{i} -> False')
