string = input()
string = string.split(' ')
new = []
for digit in string:
    num = int(digit) * -1
    new.append(num)
print(new)
