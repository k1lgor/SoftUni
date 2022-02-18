from collections import deque


def best_list_pureness(nums, k):
    nums = deque(nums)
    pureness = 0
    rotations = 0
    length = len(nums)
    for rotate in range(k + 1):
        pure = 0
        for i in range(length):
            pure += i * nums[i]
        if pure > pureness:
            pureness = pure
            rotations = rotate
        nums.appendleft(nums.pop())
    return f'Best pureness {pureness} after {rotations} rotations'


test = ([4, 3, 2, 6], 4)
result = best_list_pureness(*test)
print(result)
test = ([7, 9, 2, 5, 3, 4], 3)
result = best_list_pureness(*test)
print(result)
test = ([1, 2, 3, 4, 5], 10)
result = best_list_pureness(*test)
print(result)
