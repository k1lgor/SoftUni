start = ord(input())
end = ord(input())
chars = []
ascii_sums = []
data = [x for x in input()]

for char in data:
    if start < ord(char) < end:
        chars.append(char)
        ascii_sums.append(ord(char))
print(f'{sum(ascii_sums)}')
