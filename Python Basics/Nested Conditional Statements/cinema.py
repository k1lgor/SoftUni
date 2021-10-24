projection = input()
r = int(input())
c = int(input())

if projection == 'Premiere':
    print(f'{(12 * r * c):.2f} leva')
elif projection == 'Normal':
    print(f'{(7.5 * r * c):.2f} leva')
elif projection == 'Discount':
    print(f'{(5 * r * c):.2f} leva')
