n = float(input())
sum_total = 0.0
while True:
    if n < 0:
        print('Negative number!')
        break
    sum_total = n * 2
    print(f'Result: {sum_total:.2f}')
    n = float(input())


# n = float(input())
# sum = 0.0
# while n >= 0:
#    sum = n * 2
#    print(f'Result: {sum:.2f}')
#    n = float(input())
# while n < 0:
#    print('Negative number!')
#    break
