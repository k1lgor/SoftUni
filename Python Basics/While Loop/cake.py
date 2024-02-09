w = int(input())
l = int(input())

cake = w * l
while cake > 0:
    if (slices := input()) == 'STOP':
        print(f'{cake} pieces are left.')
        break
    cake -= int(slices)
if cake < 0:
    print(f'No more cake left! You need {abs(cake)} pieces more.')
