from math import factorial

def factorialDiv(num1, num2):
    div = factorial(num1) / factorial(num2)
    print(f'{div:.2f}')
          
num1, num2 = int(input()), int(input())
factorialDiv(num1, num2)