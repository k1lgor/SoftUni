data = [int(x)
        for x in list(map(lambda x: int(x), input().split())) if x % 2 == 0]
new_data = []

for num in data:
    if num > (sum(data) / len(data)):
        num += 1
    else:
        num -= 1
    new_data.append(num)

print(*new_data)
