numbers_list = [int(x) for x in input().split(", ")]
result = 1

for number in numbers_list:
    if number <= 5:
        result *= number
    else:
        result /= number

print(int(result))
