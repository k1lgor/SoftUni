import re

number_of_msg = int(input())
planets = {'A': [], 'D': []}

for _ in range(number_of_msg):
    data = input()

    len_chars = len(re.findall(r"[star]", data, re.IGNORECASE))
    decrypt = ''.join(chr(ord(letter) - len_chars) for letter in data)

    if cipher := re.findall(r"@([a-z]+)[^@\-!:>]*:(\d+)[^@\-!:>]*\!([ad])\![^@\-!:>]*->(\d+)", decrypt, re.IGNORECASE):
        if cipher[0][2] == 'A':
            planets['A'].append(cipher[0][0])
        else:
            planets['D'].append(cipher[0][0])

for k, v in planets.items():
    if k == 'A':
        print(f"Attacked planets: {len(v)}")
        if v != 0:
            for vv in sorted(v, key=str):
                print(f"-> {vv}")
for k, v in planets.items():
    if k == 'D':
        print(f"Destroyed planets: {len(v)}")
        if v != 0:
            for vv in sorted(v, key=str):
                print(f"-> {vv}")
