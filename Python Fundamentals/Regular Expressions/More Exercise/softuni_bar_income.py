import re

command = input()
total = 0

while 'end of shift' not in command:
    if regex := re.findall(r"%(?P<customer>[A-Z][a-z]+)%[^|$%.]*<(?P<product>\w+)>[^|$%.]*\|(?P<count>\d+)\|[^\d|$%.]*(?P<price>\d+\.?\d+)\$", command):
        print(
            f"{regex[0][0]}: {regex[0][1]} - {int(regex[0][2]) * float(regex[0][3]):.2f}")
        total += int(regex[0][2]) * float(regex[0][3])

    command = input()

print(f"Total income: {total:.2f}")
