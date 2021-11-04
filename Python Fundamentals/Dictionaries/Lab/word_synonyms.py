word_count = int(input())
DICT = {}

for _ in range(word_count):

    word = input()
    synonym = input()
    if word not in DICT:
        DICT[word] = []
    DICT[word].append(synonym)

for word in DICT:
    print(f"{word} - {', '.join(DICT[word])}")
