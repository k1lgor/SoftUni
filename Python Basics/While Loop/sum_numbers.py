n = int(input())

sum_total = 0

while n > 0:
    num = int(input())
    sum_total += num
    if sum_total >= n:
        print(sum_total)
        break
