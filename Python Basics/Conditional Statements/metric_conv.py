a = float(input())
t1 = input()
t2 = input()

if t1 == 'mm' and t2 == 'm':
    print(f'{(a / 1000):.3f}')
elif t1 == 'mm' and t2 == 'cm':
    print(f'{(a / 10):.3f}')
elif t1 == 'm' and t2 == 'cm':
    print(f'{(a * 100):.3f}')
elif t1 == 'm' and t2 == 'mm':
    print(f'{(a * 1000):.3f}')
elif t1 == 'cm' and t2 == 'mm':
    print(f'{(a * 10):.3f}')
elif t1 == 'cm' and t2 == 'm':
    print(f'{(a / 100):.3f}')
