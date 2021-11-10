data = input()
encrypted = [ord(char) + 3 for char in data]

for i in encrypted:
    print(f"{''.join(chr(i))}", end='')
