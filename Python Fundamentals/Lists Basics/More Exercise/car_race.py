time = input().split(' ')

middle = len(time) // 2 + 1
left_time = 0
right_time = 0

for i in time[:middle - 1]:
    if int(i) == 0:
        left_time *= 0.8
    left_time += int(i)

for j in time[:middle - 1:-1]:
    if int(j) == 0:
        right_time *= 0.8
    right_time += int(j)
    
if left_time < right_time:
    print(f'The winner is left with total time: {left_time:.1f}')
else:
    print(f'The winner is right with total time: {right_time:.1f}')