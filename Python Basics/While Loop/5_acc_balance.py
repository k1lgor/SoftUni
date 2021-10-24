text = input()
sum = 0
while text != 'NoMoreMoney':
    num = float(text)
    if num < 0:
        print('Invalid operation!')
        break
    sum += num
    print(f'Increase: {num:.2f}')
    text = input()
print(f'Total: {sum:.2f}')
