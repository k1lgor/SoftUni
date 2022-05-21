import re


def decrypter(n):
    LIST = []
    for _ in range(n):
        data = input()
        if match := re.match(r"^(\$|%)([A-Z][a-z]{2,})\1: \[(\d+)\]\|\[(\d+)\]\|\[(\d+)\]\|$", data):
            print(
                f"{match[2]}: {chr(int(match[3]))}{chr(int(match[4]))}{chr(int(match[5]))}")

        else:
            print("Valid message not found!")


number = int(input())
decrypter(number)
