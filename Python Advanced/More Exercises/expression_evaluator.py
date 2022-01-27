from collections import deque

data = input().split()
to_operate = deque()

for element in data:
    if element in '+-*/':
        while len(to_operate) > 1:
            first = to_operate.popleft()
            second = to_operate.popleft()
            result = 0
            if element == '+':
                result = first + second
            elif element == '-':
                result = first - second
            elif element == '*':
                result = first * second
            else:
                result = first // second
            to_operate.appendleft(result)
    else:
        to_operate.append(int(element))

print(to_operate.popleft())
