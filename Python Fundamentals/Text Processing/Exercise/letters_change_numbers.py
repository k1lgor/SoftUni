data = input()
data_list = data.split()

alphabet = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
    "e": 5,
    "f": 6,
    "g": 7,
    "h": 8,
    "i": 9,
    "j": 10,
    "k": 11,
    "l": 12,
    "m": 13,
    "n": 14,
    "o": 15,
    "p": 16,
    "q": 17,
    "r": 18,
    "s": 19,
    "t": 20,
    "u": 21,
    "v": 22,
    "w": 23,
    "x": 24,
    "y": 25,
    "z": 26,
}
final_result = 0

for i in data_list:
    first_letter = i[0]
    last_letter = i[len(i) - 1:]
    num = int(i[1:len(i) - 1])

    if first_letter.isupper():
        result1 = num / alphabet.get(first_letter.lower())
    else:
        result1 = num * alphabet.get(first_letter.lower())
    if last_letter.isupper():
        result2 = result1 - alphabet.get(last_letter.lower())
    else:
        result2 = result1 + alphabet.get(last_letter.lower())
    final_result += result2
print(f"{final_result:.2f}")
