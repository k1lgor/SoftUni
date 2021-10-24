def perfectNum(number):
    sum_divisors = sum(num for num in range(1, number) if number % num == 0)
    if (sum_divisors + number) % number == 0:
        print('We have a perfect number!')
    else:
        print('It\'s not so perfect.')
        
perfectNum(number = int(input()))