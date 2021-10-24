w = int(input())
l = int(input())

cake = w * l
while cake > 0:
    slice = input()
    if slice == 'STOP':
        print(f'{cake} pieces are left.')
        break
    cake -= int(slice)
if cake < 0:
    print(f'No more cake left! You need {abs(cake)} pieces more.')
