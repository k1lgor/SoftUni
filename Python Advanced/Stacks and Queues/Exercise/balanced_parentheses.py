data = input()
brackets = []

paired = True
for i in data:
    if i in '[{(':
        brackets.append(i)
    elif not brackets:
        paired = False
        break
    else:
        last_pop = brackets.pop()
        if f'{last_pop}{i}' not in '()[]{}':
            paired = False
            break
if paired:
    print("YES")
else:
    print("NO")
