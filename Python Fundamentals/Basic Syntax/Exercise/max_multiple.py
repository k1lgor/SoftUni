divisor = int(input())
bound = int(input())

print(max([i for i in range(divisor, bound + 1) if i % divisor == 0 and bound >= i > 0]))

# n = 0
# 
# for i in range(divisor, bound + 1):
#     if i % divisor == 0 and bound >= i > 0:
#         n = i
# print(n)
