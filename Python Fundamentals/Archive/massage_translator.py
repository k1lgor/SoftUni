import re


def translator(n):
    for _ in range(n):
        data = input()
        if match := re.match(r"!([A-Z][a-z]{2,})!\:\[([a-zA-Z]{8,})\]", data):
            print(f"{match[1]}: {' '.join([str(ord(i)) for i in match[2]])}")
        else:
            print("The message is invalid")


number = int(input())
translator(number)
