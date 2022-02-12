from functools import reduce


def operate(operand, *args):
    if operand == '*':
        return reduce(lambda x, y: x * y, args)
    elif operand == '+':
        return sum(args)
    elif operand == '-':
        return reduce(lambda x, y: x - y, args)
    elif operand == '/':
        try:
            return reduce(lambda x, y: x / y, args)
        except Exception:
            return None


print(operate("+", 1, 2, 3))
print(operate("*", 3, 4))
print(operate("/", 1, 2, 0))
