string = input()
string = string.split(' ')
new = []
for index, digit in enumerate(string):
    num = int(digit) * -1
    new.append(num)
print(new)