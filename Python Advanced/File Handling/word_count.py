import re


def printer(words):
    for k, v in sorted(words.items(), key=lambda x: (-x[1])):
        print(f"{k} - {v}")


def finder(searched_words):
    words = {}
    with open('input.txt') as file:
        text = file.read()
        for x in searched_words:
            count = len((re.findall(fr"\b{x}\b", text, re.IGNORECASE)))
            words[x] = count
    return printer(words)


def counter():
    searched_words = []
    with open('words.txt') as file:
        searched_words.extend(iter(file.read().split()))
    return finder(searched_words)


counter()
