def tribonacci(n):

    if n < 1:
        return
    first = 1
    print(first, end=' ')
    if n >= 2:
        second = 1
        print(second, end=' ')
    if n >= 3:
        third = 2
        print(third, end=' ')

    for _ in range(3, n):
        curr = first + second + third
        first = second
        second = third
        third = curr

        print(curr, end=' ')


n = int(input())
tribonacci(n)
