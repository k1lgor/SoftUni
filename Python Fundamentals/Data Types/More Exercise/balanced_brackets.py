n = int(input())
counter1 = 0
counter2 = 0
cons = 0
for _ in range(n):
    if cons == 2:
        break
    word = input()
    if word in "(":
        counter1 += 1
        if word == "(":
            cons += 1
    if word in ")":
        counter2 += 1
    if word != "(":
        cons = 0
if counter1 == counter2:
    print('BALANCED')
else:
    print('UNBALANCED')
