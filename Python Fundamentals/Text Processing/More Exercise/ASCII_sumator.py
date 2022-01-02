def asci(start, end):

    chars = []
    ascii_sums = []
    data = list(input())

    for char in data:
        if start < ord(char) < end:
            chars.append(char)
            ascii_sums.append(ord(char))
    print(f'{sum(ascii_sums)}')


asci(ord(input()), ord(input()))
