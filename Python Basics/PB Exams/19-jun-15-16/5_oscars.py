actor = input()
academy_points = float(input())
jury = int(input())
jury_name = ''
jury_points = 0
cur_points = 0
for i in range(jury):
    jury_name = input()
    jury_points = float(input())

    name_len = len(jury_name)
    cur_points = name_len * jury_points / 2
    academy_points += cur_points

    if academy_points > 1250.5:
        print(f'Congratulations, {actor} got a nominee for leading role with {academy_points:.1f}!')
        break
if 1250.5 > academy_points:
    print(f'Sorry, {actor} you need {(1250.5 - academy_points):.1f} more!')