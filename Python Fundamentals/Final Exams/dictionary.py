def add(w, d):
    for i in d:
        word, defi = i.split(":")
        if word in w:
            w[word].append(defi)
        else:
            w[word] = [defi]


data = input().split(" | ")
test_words = input().split(" | ")
words = {}
command = input()

add(words, data)

if command == 'Test':
    for i in test_words:
        for k, v in words.items():
            if k == i:
                print(f"{k}:")
                for vv in sorted(v, key=lambda x: -len(x)):
                    print(f" -{vv.strip()}")
elif command == 'Hand Over':
    only_words = [k for k in sorted(words.keys())]
    print(*only_words)
