name = input()

area = ''
points = 301
success = 0
fail = 0
while area != 'Retire':

    if points == 0:
        print(f'{name} won the leg with {success} shots.')
        break
    area = input()
    if area == 'Retire':
        print(f'{name} retired after {fail} unsuccessful shots.')
        break
    cur_points = int(input())
    if area == 'Triple':
        cur_points *= 3
    elif area == 'Double':
        cur_points *= 2

    if cur_points > points:
        fail += 1
        continue
    else:
        success += 1
    points -= cur_points
