data = input()
paran = []

for i, d in enumerate(data):
    if d == '(':
        paran.append(i)
    elif d == ')':
        closing_bracket = i
        opening_bracket = paran.pop()
        print(data[opening_bracket:closing_bracket + 1])
