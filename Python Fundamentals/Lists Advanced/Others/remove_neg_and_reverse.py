nums = list(map(int, input().split()))
nums = [x for x in nums if x >= 0]
if not nums:
    print('empty')
else:
    nums.reverse()
    print(*nums, sep=' ')
