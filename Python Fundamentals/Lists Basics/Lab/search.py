n = int(input())
word = input()
List = []

for _ in range(n):
    string = input()
    List.append(string)
print(List)
for i in range(len(List) - 1, -1, -1):
    element = List[i]
    if word not in element:
        List.remove(element)
print(List)