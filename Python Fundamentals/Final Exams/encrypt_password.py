import re


def encrypt(n):
    for _ in range(n):
        data = input()
        if match := re.match(r"^(\w*|\W*)>(\d+)\|([a-z]+)\|([A-Z]+)\|([^\<\>]+)<\1$", data):
            print(f"Password: {match[2]}{match[3]}{match[4]}{match[5]}")
        else:
            print("Try another password!")


number = int(input())
encrypt(number)
