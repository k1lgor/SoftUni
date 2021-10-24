fruit = input()
day = input()
qnty = float(input())

if fruit == 'banana':
    if day in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']:
        qnty *= 2.5
        print(f'{qnty:.2f}')
    elif day in ['Saturday', 'Sunday']:
        qnty *= 2.7
        print(f'{qnty:.2f}')
    else:
        print('error')
elif fruit == 'apple':
    if day in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']:
        qnty *= 1.2
        print(f'{qnty:.2f}')
    elif day in ['Saturday', 'Sunday']:
        qnty *= 1.25
        print(f'{qnty:.2f}')
    else:
        print('error')
elif fruit == 'orange':
    if day in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']:
        qnty *= 0.85
        print(f'{qnty:.2f}')
    elif day in ['Saturday', 'Sunday']:
        qnty *= 0.9
        print(f'{qnty:.2f}')
    else:
        print('error')
elif fruit == 'grapefruit':
    if day in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']:
        qnty *= 1.45
        print(f'{qnty:.2f}')
    elif day in ['Saturday', 'Sunday']:
        qnty *= 1.6
        print(f'{qnty:.2f}')
    else:
        print('error')
elif fruit == 'kiwi':
    if day in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']:
        qnty *= 2.7
        print(f'{qnty:.2f}')
    elif day in ['Saturday', 'Sunday']:
        qnty *= 3
        print(f'{qnty:.2f}')
    else:
        print('error')
elif fruit == 'pineapple':
    if day in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']:
        qnty *= 5.5
        print(f'{qnty:.2f}')
    elif day in ['Saturday', 'Sunday']:
        qnty *= 5.6
        print(f'{qnty:.2f}')
    else:
        print('error')
elif fruit == 'grapes':
    if day in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']:
        qnty *= 3.85
        print(f'{qnty:.2f}')
    elif day in ['Saturday', 'Sunday']:
        qnty *= 4.2
        print(f'{qnty:.2f}')
    else:
        print('error')
else:
    print('error')
