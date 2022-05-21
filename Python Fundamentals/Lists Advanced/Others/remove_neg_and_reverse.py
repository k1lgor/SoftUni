nums = list(map(int, input().split()))
if nums := [x for x in nums if x >= 0]:
    nums.reverse()
    print(*nums, sep=' ')
else:
    print('empty')
