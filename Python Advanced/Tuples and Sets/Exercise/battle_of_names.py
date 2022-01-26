num = int(input())
even, odd = set(), set()

for row in range(1, num + 1):
    ascii_sum = sum(ord(x) for x in input()) // row
    if ascii_sum % 2 == 0:
        even.add(ascii_sum)
    else:
        odd.add(ascii_sum)
    ascii_sum = 0

if sum(even) == sum(odd):
    [print(', '.join(str(x) for x in even.union(odd)))]
elif sum(odd) > sum(even):
    [print(', '.join(str(x) for x in odd.difference(even)))]
else:
    [print(', '.join(str(x) for x in even.symmetric_difference(odd)))]
