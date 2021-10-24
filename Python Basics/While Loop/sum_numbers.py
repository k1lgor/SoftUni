n = int(input())

sum = 0

while n > 0:
    num = int(input())
    sum += num
    if sum >= n:
        print(sum)
        break
