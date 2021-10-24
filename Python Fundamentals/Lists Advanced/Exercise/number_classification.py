numbers = input().split(', ')
positive = ', '.join(num for num in numbers if int(num) >= 0)
negative = ', '.join(num for num in numbers if int(num) < 0)
even = ', '.join(num for num in numbers if int(num) % 2 == 0)
odd = ', '.join(num for num in numbers if int(num) % 2 != 0)
print(f'Positive: {positive}\nNegative: {negative}\nEven: {even}\nOdd: {odd}')
