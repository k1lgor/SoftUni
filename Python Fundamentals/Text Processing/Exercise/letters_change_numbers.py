def change(data):
    final_result = 0
    for i in data:
        first_letter = i[0]
        last_letter = i[len(i) - 1:]
        num = int(i[1:len(i) - 1])

        def fl(fl, n):
            return (
                n / alphabet.get(fl.lower())
                if fl.isupper()
                else n * alphabet.get(fl.lower())
            )
        fl(first_letter, num)

        def ll(ll, r1):
            return (
                r1 - alphabet.get(last_letter.lower())
                if ll.isupper()
                else r1 + alphabet.get(last_letter.lower())
            )
        ll(last_letter, fl(first_letter, num))
        final_result += ll(last_letter, fl(first_letter, num))
    print(f"{final_result:.2f}")


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


change(input().split())
