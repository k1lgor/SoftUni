data = list(input().split(' '))
nums = [data.pop() for _ in range(len(data))]
print(*nums)
