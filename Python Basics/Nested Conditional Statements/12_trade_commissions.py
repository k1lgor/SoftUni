city = input()
sales = float(input())

if 0 <= sales <= 500:
    if city == 'Sofia':
        print(f'{(sales * 0.05):.2f}')
    elif city == 'Varna':
        print(f'{(sales * 0.045):.2f}')
    elif city == 'Plovdiv':
        print(f'{(sales * 0.055):.2f}')
    else:
        print('error')
elif 500 < sales <= 1000:
    if city == 'Sofia':
        print(f'{(sales * 0.07):.2f}')
    elif city == 'Varna':
        print(f'{(sales * 0.075):.2f}')
    elif city == 'Plovdiv':
        print(f'{(sales * 0.08):.2f}')
    else:
        print('error')
elif 1000 < sales <= 10000:
    if city == 'Sofia':
        print(f'{(sales * 0.08):.2f}')
    elif city == 'Varna':
        print(f'{(sales * 0.1):.2f}')
    elif city == 'Plovdiv':
        print(f'{(sales * 0.12):.2f}')
    else:
        print('error')
elif sales > 10000:
    if city == 'Sofia':
        print(f'{(sales * 0.12):.2f}')
    elif city == 'Varna':
        print(f'{(sales * 0.13):.2f}')
    elif city == 'Plovdiv':
        print(f'{(sales * 0.145):.2f}')
    else:
        print('error')
else:
    print('error')
