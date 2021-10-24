string = input()
result = ''

ZIP = []
NUM = [x for x in string if x.isdigit()]
STRING = [x for x in string if not x.isdigit()]
ODD = [int(d) for i, d in enumerate(NUM) if i % 2 != 0]
EVEN = [int(d) for i, d in enumerate(NUM) if i % 2 == 0]

for i in zip(EVEN, ODD):
    ZIP.extend(i)

ZIP = [str(x) for x in ZIP]
for i, d in enumerate(ZIP):
    if i % 2 == 0:
        result += ''.join(STRING[:int(d)])
    STRING = STRING[int(d):]
print(result)
