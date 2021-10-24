start = int(input())
end = int(input())

for number in range(start, end + 1):
    string = str(number)
    even = 0
    odd = 0
    for index, digit in enumerate(string):
        if index % 2 == 0:
            even += int(digit)
        else:
            odd += int(digit)

    if even == odd:
        print(number, end=' ')
