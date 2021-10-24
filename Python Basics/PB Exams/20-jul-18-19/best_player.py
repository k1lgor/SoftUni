name = ''
golaso = 0
best_golaso = 0
best_name = ''
while name != 'END':
    name = input()
    if name == 'END':
        break
    golaso = int(input())
    if golaso > best_golaso:
        best_golaso = golaso
        best_name = name
    if golaso >= 10:
        break
print(f'{best_name} is the best player!')
if golaso >= 3:
    print(f'He has scored {best_golaso} goals and made a hat-trick !!!')
else:
    print(f'He has scored {best_golaso} goals.')