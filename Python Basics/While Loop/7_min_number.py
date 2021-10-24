import sys
text = input()
num = sys.maxsize

while text != 'Stop':
    a = int(text)
    if a < num:
        num = a
    text = input()
print(num)
