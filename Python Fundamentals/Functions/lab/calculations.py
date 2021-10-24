def solve(a, b, operator):
    if operator == 'multiply':
        result = a * b
    elif operator == 'divide':
        result = a // b
    elif operator == 'add':
        result = a + b
    elif operator == 'subtract':
        result = a - b
    return result
operator = input()
a = int(input())
b = int(input())
print(solve(a, b, operator))