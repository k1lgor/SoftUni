import re

while data := input():
    if valid_emails := [mail.group() for mail in re.finditer(r"www.([a-zA-Z0-9\-]+).([\.][a-z]+)+", data)]:
        print(*valid_emails)
