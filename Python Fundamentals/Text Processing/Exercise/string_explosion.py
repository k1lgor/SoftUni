data = input().split(">")
explosion = 0
char = ''
result = []

for i in data:
    if i[0].isdigit():
        explosion += int(i[0])
        if explosion >= len(i):
            explosion -= len(i)
            char = '>'
        else:
            char = '>' + ''.join(i[explosion:])
            explosion = 0
    else:
        char = i
    result.append(char)
print(''.join(result))
