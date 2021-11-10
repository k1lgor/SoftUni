data = input().split(", ")
allowed = []

for word in data:
    if 3 <= len(word) <= 16:
        result = ''.join(
            char
            for char in word
            if char.isalnum() or char == '-' or char == '_'
        )

        if word == result:
            allowed.append(word)
print('\n'.join(allowed))
