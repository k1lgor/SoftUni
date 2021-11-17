import re

data = input()

while data:

    valid_emails = [mail.group() for mail in re.finditer(
        r"www.([a-zA-Z0-9\-]+).([\.][a-z]+)+", data)]
    if valid_emails:
        print(*valid_emails)
    data = input()
