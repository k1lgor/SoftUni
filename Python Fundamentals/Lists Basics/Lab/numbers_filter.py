n = int(input())

nums = []
for _ in range(n):
    num = int(input())
    nums.append(num)
command = input()
filter = [
    i
    for i in nums
    if command == 'even'
    and i % 2 == 0
    or command != 'even'
    and command == 'negative'
    and i < 0
    or command != 'even'
    and command != 'negative'
    and command == 'odd'
    and i % 2 != 0
    or command != 'even'
    and command != 'negative'
    and command != 'odd'
    and command == 'positive'
    and i >= 0
]
# if command == 'positive':
#     for i in nums:
#         if i >= 0:
#             filter.append(i)
# elif command == 'negative':
#     for i in nums:
#         if i < 0:
#             filter.append(i)
# elif command == 'even':
#     for i in nums:
#         if i % 2 == 0:
#             filter.append(i)
# elif command == 'odd':
#     for i in nums:
#         if i % 2 != 0:
#             filter.append(i)
print(filter)