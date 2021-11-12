data = input()
result = ""
symbols = ""
counter = []

for index, letter in enumerate(data):
    if not letter.isdigit():
        if letter.lower() not in counter:
            counter.append(letter.lower())
        symbols += letter
    if letter.isdigit():
        old_digit = ""
        if old_digit.isdigit() and letter.isdigit():
            continue
        digit = ""
        new_data = data[index:]
        for d in new_data:
            if d.isdigit():
                digit += d
            else:
                break
        old_digit = letter
        result += symbols.upper() * int(digit)
        symbols = ""

print(f"Unique symbols used: {len(counter)}\n{result}")
