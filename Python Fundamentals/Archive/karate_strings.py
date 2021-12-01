data = input().split(">")
strength = 0
char = ''
result = []

for i in data:
    if i[0].isdigit():
        strength += int(i[0])
        if strength >= len(i):
            strength -= len(i)
            char = '>'
        else:
            char = '>' + ''.join(i[strength:])
            strength = 0
    else:
        char = i
    result.append(char)
print(''.join(result))
