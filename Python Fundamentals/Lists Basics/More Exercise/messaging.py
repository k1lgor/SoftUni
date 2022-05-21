num = input().split(' ')
string = input()
output = ''

for i in range(len(num)):
    index = sum(int(d) for d in num[i])

    if index > len(string):
        index -= len(string)

    output += string[index]
    string = string[:index] + string[index + 1:]

print(output)
