string = input().split()
LIST = []

for word in string:

    only_int = int(''.join(digit for digit in word if digit.isdigit()))
    length_int = len(str(only_int))
    char = chr(only_int)
    word = [word[length_int:]]
    word.insert(0, char)
    word = ''.join(word)
    length_word = len(word)
    second_letter = word[1]
    last_letter = word[length_word - 1]
    word = list(word)
    word.pop(1) and word.insert(1, last_letter)
    word.pop() and word.append(second_letter)
    LIST.append(''.join(word))

print(' '.join(LIST))
