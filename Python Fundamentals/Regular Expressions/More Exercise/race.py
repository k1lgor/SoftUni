import re

names = list(input().split(", "))
command = input()
regex_names = {}

while 'end of race' not in command:
    name = ''.join([x.group() for x in re.finditer(r"([a-zA-Z]+)", command)])
    dist = sum((int(x.group()) for x in re.finditer(r"\d", command)))
    if name in names:
        if name in regex_names:
            regex_names[name] += dist
        else:
            regex_names[name] = dist

    command = input()
places = {}
winners = [k for k, v in sorted(regex_names.items(), key=lambda x: -(x[1]))]
print(
    f"1st place: {winners[0]}\n2nd place: {winners[1]}\n3rd place: {winners[2]}")
