def sum_numbers(num1, num2):
    return num1 + num2


def multiply_numbers(num1, num2):
    return num1 * num2


def func_executor(*args):
    return [ref(*params) for ref, params in args]


print(func_executor((sum_numbers, (1, 2)), (multiply_numbers, (2, 4))))
