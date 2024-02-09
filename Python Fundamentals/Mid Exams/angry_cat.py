rating = list(map(lambda x: int(x), input().split(', ')))
entry_point = int(input())

if (type_items := input()) == 'cheap':
    left = [i for i in rating[:entry_point] if i < rating[entry_point]]
    right = [i for i in rating[entry_point + 1:] if i < rating[entry_point]]
else:
    left = [i for i in rating[:entry_point] if i >= rating[entry_point]]
    right = [i for i in rating[entry_point + 1:] if i >= rating[entry_point]]

if sum(left) >= sum(right):
    print(f'Left - {sum(left)}')
else:
    print(f'Right - {sum(right)}')
