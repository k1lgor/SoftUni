kozunak = int(input())
name = ''
grade = ''
cur_points = 0
best_points = 0
best_name = ''
for i in range(kozunak):
    name = input()
    while grade != 'Stop':
        grade = input()
        if grade == 'Stop':
            break
        cur_points += int(grade)
    print(f'{name} has {cur_points} points.')
    if cur_points > best_points:
        best_points = cur_points
        best_name = name
        print(f'{best_name} is the new number 1!')
    cur_points = 0
    grade = ''

print(f'{best_name} won competition with {best_points} points!')