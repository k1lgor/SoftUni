words = input().split(" ")
DICT = {}

for word in words:
    single_word = word.lower()
    if single_word not in DICT:
        DICT[single_word] = 0
    DICT[single_word] += 1

for k, v in DICT.items():
    if v % 2 != 0:
        print(k, end=' ')
