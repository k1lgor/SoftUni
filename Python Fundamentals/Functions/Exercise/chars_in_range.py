def charRange(char1, char2):

    List = [chr(letter) for letter in range(ord(char1) + 1, ord(char2))]
    print(' '.join(list(map(str, List))))
    return List

char1 = input()
char2 = input()
charRange(char1, char2)