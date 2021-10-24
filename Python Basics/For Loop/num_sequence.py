import sys
nl = '\n'
small = sys.maxsize
big = -sys.maxsize
for _ in range(int(input())):
    n = int(input())
    if n > big:
        big = n
    if n < small:
        small = n
print(f'Max number: {big}{nl}Min number: {small}')
