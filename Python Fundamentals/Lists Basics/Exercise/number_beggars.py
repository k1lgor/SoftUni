int_string = input()
count = int(input())

string = int_string.split(', ')
sum1 = 0
List = []
for i in range(count):
    beggars = string[i::count]
    for d in beggars:
        sum1 += int(d)
    List.append(sum1)
    sum1 = 0
print(List)
