from collections import deque


def math_operations(*args, **kwargs):
    LIST = deque(args)

    while LIST:

        kwargs['a'] += LIST.popleft()
        if not LIST:
            break
        kwargs['s'] -= LIST.popleft()
        if not LIST:
            break
        num = LIST.popleft()
        if num != 0:
            kwargs['d'] /= num
        if not LIST:
            break
        kwargs['m'] *= LIST.popleft()
        if not LIST:
            break

    return kwargs


print(math_operations(2, 12, 0, -3, 6, -20, -11, a=1, s=7, d=33, m=15))
print(math_operations(-1, 0, 1, 0, 6, -2, 80, a=0, s=0, d=0, m=0))
print(math_operations(6, a=0, s=0, d=0, m=0))
