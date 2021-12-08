import re


def decrypter(n):
    LIST = []
    for _ in range(n):
        data = input()
        match = re.match(
            r"^(\$|%)([A-Z][a-z]{2,})\1: \[(\d+)\]\|\[(\d+)\]\|\[(\d+)\]\|$", data)

        if match:
            print(
                f"{match.group(2)}: {chr(int(match.group(3)))}{chr(int(match.group(4)))}{chr(int(match.group(5)))}")
        else:
            print("Valid message not found!")


number = int(input())
decrypter(number)
