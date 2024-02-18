import re


def register(n, c):
    for _ in range(n):
        data = input()

        if match := re.match(r"U\$([A-Z][a-z]{2,})U\$P\@\$([a-z]{5,}\d+)P\@\$", data):
            c += 1
            print("Registration was successful")
            print(f"Username: {match[1]}, Password: {match[2]}")
        else:
            print("Invalid username or password")

    print(f"Successful registrations: {c}")


number = int(input())
counter = 0
register(number, counter)
