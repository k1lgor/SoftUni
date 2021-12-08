import re


def egg(data):
    match = re.findall(r"([@|#]{1,})([a-z]{3,})\W*\/{1,}(\d+)\/{1,}", data)
    for i in match:
        print(f"You found {i[2]} {i[1]} eggs!")


data = input()
egg(data)
