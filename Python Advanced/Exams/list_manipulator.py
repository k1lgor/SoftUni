from collections import deque


def list_manipulator(nums, *args):
    nums = deque(nums)
    args = list(args)
    command, *tokens = args
    if command == 'add':
        if tokens[0] == 'beginning':
            for x in sorted(args[2:], reverse=True):
                nums.appendleft(x)
        elif tokens[0] == 'end':
            for x in args[2:]:
                nums.append(x)
    elif command == 'remove':
        if tokens[0] == 'beginning':
            if len(tokens) < 2:
                nums.popleft()
            elif len(tokens) >= 2:
                for x in range(tokens[1]):
                    nums.popleft()
        if tokens[0] == 'end':
            if len(tokens) < 2:
                nums.pop()
            elif len(tokens) >= 2:
                for x in range(tokens[1]):
                    nums.pop()
    return list(nums)


# print(list_manipulator([1, 2, 3], "remove", "end"))
# print(list_manipulator([1, 2, 3], "remove", "beginning"))
# print(list_manipulator([1, 2, 3], "add", "beginning", 20))
# print(list_manipulator([1, 2, 3], "add", "end", 30))
print(list_manipulator([1, 2, 3], "remove", "end", 2))
print(list_manipulator([1, 2, 3], "remove", "beginning", 2))
print(list_manipulator([1, 2, 3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1, 2, 3], "add", "end", 30, 40, 50))
