data = input().split("|")

text = ""
old = ""
for i in data:
    counter_0 = 0
    counter_1 = 0
    multiplier = 0
    coun1 = 1
    for coun0, j in enumerate(i):
        if 0 <= coun0 < len(i) and 0 <= coun1 < len(i) and i[coun0] == i[coun1]:
            multiplier += 1
        if j == "0":
            counter_0 += 1
        else:
            counter_1 += 1
        coun1 += 1
    text += chr(counter_0 * 3 + counter_1 * 5 + multiplier)
print(text)
