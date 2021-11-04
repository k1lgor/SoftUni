DICT = {}
word1 = input()

while word1 != 'stop':

    word2 = input()

    if word1 not in DICT:
        DICT[word1] = 0
    DICT[word1] += int(word2)

    word1 = input()

for k, v in DICT.items():
    print(f"{k} -> {v}")
