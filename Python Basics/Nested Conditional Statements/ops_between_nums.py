n1 = int(input())
n2 = int(input())
operand = input()
result = 0.0

if operand == '+':
    result = n1 + n2
    if result % 2 == 0:
        print(f'{n1} {operand} {n2} = {result} - even')
    else:
        print(f'{n1} {operand} {n2} = {result} - odd')
elif operand == '-':
    result = n1 - n2
    if result % 2 == 0:
        print(f'{n1} {operand} {n2} = {result} - even')
    else:
        print(f'{n1} {operand} {n2} = {result} - odd')
elif operand == '*':
    result = n1 * n2
    if result % 2 == 0:
        print(f'{n1} {operand} {n2} = {result} - even')
    else:
        print(f'{n1} {operand} {n2} = {result} - odd')
elif operand == '/':
    if n2 == 0:
        print(f"Cannot divide {n1} by zero")
    else:
        result = n1 / n2
        print(f'{n1} {operand} {n2} = {result:.2f}')
elif operand == '%':
    if n2 == 0:
        print(f"Cannot divide {n1} by zero")
    else:
        result = n1 % n2
        print(f'{n1} {operand} {n2} = {result}')
