n = int(input())
text = input()

if n >= 100:
    print(f'{(n * 0.06):.2f}')
elif 20 <= n < 100:
    print(f'{(n * 0.09):.2f}')
else:
    if text == 'day':
        print(f'{(n * 0.79 + 0.7):.2f}')
    else:
        print(f'{(n * 0.9 + 0.7):.2f}')
