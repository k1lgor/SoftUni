nums = list(map(float, input().split()))
index = 0

while index < len(nums) - 1:
    if nums[index] == nums[index + 1]:
        nums[index] *= 2
        nums.pop(index + 1)
        
        if index > 0:
            index -= 1
    else:
        index += 1
        
print(*nums, sep=' ')


