import re


def encrypt(n):
    for _ in range(n):
        data = input()
        match = re.match(
            r"^(\w*|\W*)>(\d+)\|([a-z]+)\|([A-Z]+)\|([^\<\>]+)<\1$", data)

        if match:
            print(
                f"Password: {match.group(2)}{match.group(3)}{match.group(4)}{match.group(5)}")
        else:
            print("Try another password!")


number = int(input())
encrypt(number)
