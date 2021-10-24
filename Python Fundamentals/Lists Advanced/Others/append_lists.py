nums = input().split("|")
nums2 = []
for i in nums[::-1]:
    nums2 += map(str, i.split())
print(*nums2, sep=' ')
