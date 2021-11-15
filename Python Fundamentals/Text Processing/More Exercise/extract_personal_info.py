num = int(input())

for _ in range(num):
    data = input()
    name1 = data.index("@")
    name2 = data.index("|")
    age1 = data.index("#")
    age2 = data.index("*")
    name = data[name1 + 1:name2]
    age = data[age1 + 1:age2]
    print(f"{name} is {age} years old.")
