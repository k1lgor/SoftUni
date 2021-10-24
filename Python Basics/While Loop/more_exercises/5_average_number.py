n = int(input())
counter = 0
summary = 0
while n > counter:
    nn = int(input())
    summary += nn
    counter += 1
print(f'{(summary / n):.2f}')
