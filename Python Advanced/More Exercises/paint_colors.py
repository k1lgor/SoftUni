from collections import deque


data = deque(input().split())

colors = []

while data:
    if len(data) > 1:
        first = data.popleft()
        last = data.pop()
        if first + last in ['red', 'yellow', 'blue', 'orange', 'purple', 'green']:
            color = first + last
        else:
            color = last + first
    else:
        color = data.pop()
    if color not in ['red', 'yellow', 'blue', 'orange', 'purple', 'green']:
        first = first[:len(first)-1]
        last = last[:len(last)-1]
        if first:
            data.insert(len(data) // 2, first)
        if last:
            data.insert(len(data) // 2, last)
    else:
        colors.append(color)
if 'orange' in colors and ('red' not in colors or 'yellow' not in colors):
    colors.remove('orange')
if 'purple' in colors and ('red' not in colors or 'blue' not in colors):
    colors.remove('purple')
if 'green' in colors and ('yellow' not in colors or 'blue' not in colors):
    colors.remove('green')
print(colors)
