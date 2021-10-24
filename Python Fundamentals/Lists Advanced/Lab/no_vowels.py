vowels = ['a', 'A', 'e', 'E', 'o', 'O', 'i', 'I', 'u', 'U']
no_vowels = ''.join(letter for letter in input() if letter not in vowels)
print(no_vowels)
