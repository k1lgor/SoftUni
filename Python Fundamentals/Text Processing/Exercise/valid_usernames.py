def username(data, allwd):

    for word in data:
        if 3 <= len(word) <= 16:
            result = ''.join(
                char
                for char in word
                if char.isalnum() or char == '-' or char == '_'
            )

            if word == result:
                allwd.append(word)


allowed = []
username(input().split(", "), allowed)
print('\n'.join(allowed))
