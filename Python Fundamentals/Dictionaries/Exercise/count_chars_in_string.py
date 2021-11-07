word = input()
DICT = {}
for i in range(len(word)):
    if word[i] == " ":
        continue
    elif word[i] not in DICT:
        DICT[word[i]] = 0
    DICT[word[i]] += 1

for k, v in DICT.items():
    print(f"{k} -> {v}")
