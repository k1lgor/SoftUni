nums = list(map(int, input().split()))

avr = sum(nums) / len(nums)

nums = sorted((num for num in nums if num > avr), reverse=True)
if not len(nums) == 0:
    print(*nums[:5], sep=" ")
else:
    print("No")
