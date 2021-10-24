import sys
n = int(input())
sum = 0
max_num = -sys.maxsize
for _ in range(n):
    num = int(input())
    sum += num
    if num > max_num:
        max_num = num
sum -= max_num
if sum == max_num:
    print(f'Yes\nSum = {max_num}')
else:
    print(f'No\nDiff = {abs(sum - max_num)}')
