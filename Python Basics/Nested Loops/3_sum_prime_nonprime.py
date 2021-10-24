n = ''
num = 0
prime = 0
nonprime = 0
while n != 'stop':
    n = input()
    if n == 'stop':
        break
    num = int(n)
    if num < 0:
        print('Number is negative.')
        continue
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                nonprime += num
                break
        else:
            prime += num
    else:
        prime += num

print(f'Sum of all prime numbers is: {prime}\nSum of all non prime numbers is: {nonprime}')
