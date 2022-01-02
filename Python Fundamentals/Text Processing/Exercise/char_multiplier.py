data = input().split()

max_len_word = max(len(data[0]), len(data[1]))
min_len_word = min(len(data[0]), len(data[1]))
result = sum(ord(data[0][index]) * ord(data[1][index]) for index in range(min_len_word))

for index in range(min_len_word, max_len_word):
    if len(data[0]) > len(data[1]):
        result += ord(data[0][index])
    elif len(data[0]) < len(data[1]):
        result += ord(data[1][index])

print(result)
