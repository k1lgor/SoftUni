import re

data = sorted(''.join(input().split()).split(','))

for name in data:
    HP = sum(ord(y) for y in [x.group()
                              for x in re.finditer(r"([^ 0-9-+*/.])", name)])
    DMG = sum(float(x.group())
              for x in re.finditer(r"([-+]?\d+(\.\d+)?)", name))

    multi_divide = re.findall(r"\*|\/", name)
    for sign in multi_divide:
        if sign == '*':
            DMG *= 2
        else:
            DMG /= 2
    print(f"{name} - {HP} health, {DMG:.2f} damage")
