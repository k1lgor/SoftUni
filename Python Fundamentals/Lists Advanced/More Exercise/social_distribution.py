nums = list(map(lambda x: int(x), input().split(', ')))
min_wealth = int(input())

for num in nums:

    if num < min_wealth:
        distr = min_wealth - num
        if max(nums) - distr >= min_wealth:
            nums[nums.index(max(nums))] -= distr
            num += distr

if sum(nums) >= len(nums) * min_wealth:
    print(nums)
else:
    print('No equal distribution possible')
