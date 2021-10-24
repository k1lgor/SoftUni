key = int(input())
lines = int(input())

final = ''
for _ in range(lines):
    letter = input()
    dex = ord(letter) + key
    final += chr(dex)

print(final)