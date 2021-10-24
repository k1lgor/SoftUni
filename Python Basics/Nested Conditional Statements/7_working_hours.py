hr = int(input())
day = input()

if day in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']:
    if 10 <= hr <= 18:
        print('open')
    else:
        print('closed')
else:
    print('closed')
