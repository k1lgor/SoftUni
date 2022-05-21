text = input()
sum_total = 0
while text != 'NoMoreMoney':
    num = float(text)
    if num < 0:
        print('Invalid operation!')
        break
    sum_total += num
    print(f'Increase: {num:.2f}')
    text = input()
print(f'Total: {sum_total:.2f}')
