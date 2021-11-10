data = input().split()
s1 = data[0]
s2 = data[1]

max_len_word = max(len(s1), len(s2))
min_len_word = min(len(s1), len(s2))
result = sum(ord(s1[index]) * ord(s2[index]) for index in range(min_len_word))

for index in range(min_len_word, max_len_word):
    if len(s1) > len(s2):
        result += ord(s1[index])
    elif len(s1) < len(s2):
        result += ord(s2[index])

print(result)
