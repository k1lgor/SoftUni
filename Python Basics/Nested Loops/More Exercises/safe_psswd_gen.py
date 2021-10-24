n1 = int(input())
n2 = int(input())
max_pass = int(input())
counter = 0
first_last = 35
second_fourth = 64
for i in range(1, n1 + 1):
    for j in range(1, n2 + 1):
        counter += 1
        if counter > max_pass:
            break
        if first_last > 55:
            first_last = 35
        if second_fourth > 96:
            second_fourth = 64

        print(
            f'{chr(first_last)}{chr(second_fourth)}{i}{j}{chr(second_fourth)}{chr(first_last)}', end='|')
        first_last += 1
        second_fourth += 1
