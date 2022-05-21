n = int(input())

nums = []
for _ in range(n):
    num = int(input())
    nums.append(num)
command = input()
filters = [
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
print(filters)
