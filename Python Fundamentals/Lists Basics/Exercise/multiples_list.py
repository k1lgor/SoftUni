factor = int(input())
count = int(input())

List = []
for i in range(1, count + 1):
    num = i * factor
    List.append(num)
print(List)