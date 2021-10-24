colored_eggs = int(input())

red = 0
orange = 0
blue = 0
green = 0
text = ''
max_eggs = 0
color = ''
for i in range(colored_eggs):
    text = input()
    if text == 'red':
        red += 1
    elif text == 'orange':
        orange += 1
    elif text == 'blue':
        blue += 1
    elif text == 'green':
        green += 1
if red > max_eggs:
    max_eggs = red
    color = 'red'
if orange > max_eggs:
    max_eggs = orange
    color = 'orange'
if blue > max_eggs:
    max_eggs = blue
    color = 'blue'
if green > max_eggs:
    max_eggs = green
    color = 'green'
print(f'Red eggs: {red}\nOrange eggs: {orange}\nBlue eggs: {blue}\nGreen eggs: {green}\nMax eggs: {max_eggs} -> {color}')