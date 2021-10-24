name = ''
win_name = ''
best_points = 0
while name != 'Stop':
    name_len = len(name)
    points = 0
    for _ in range(name_len):
        for index, digit in enumerate(name):
            number = int(input())
            points += 10 if digit == chr(number) else 2
        break
    if points >= best_points:
        best_points = points
        win_name = name

    name = input()

print(f'The winner is {win_name} with {best_points} points!')
