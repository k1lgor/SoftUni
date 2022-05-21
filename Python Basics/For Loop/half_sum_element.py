import sys
n = int(input())
total = 0
max_num = -sys.maxsize
for _ in range(n):
    num = int(input())
    total += num
    if num > max_num:
        max_num = num
total -= max_num
if total == max_num:
    print(f'Yes\nSum = {max_num}')
else:
    print(f'No\nDiff = {abs(total - max_num)}')
