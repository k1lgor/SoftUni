num = input()
big_num = []

for digit in num:
    big_num.append(int(digit))
    big_num.sort()
    big_num.reverse()

num2 = int(''.join(map(str, big_num)))
print(num2)
