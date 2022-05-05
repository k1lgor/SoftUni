import re


class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


email = input()

while email:

    valid_emails = re.findall(
        r"([a-z]+)(@?)([a-z]+)?(.*)", email)
    if len(valid_emails[0][0]) <= 4:
        raise NameTooShortError("Name must be more than 4 characters")
    if not valid_emails[0][1]:
        raise MustContainAtSymbolError("Email must contain @")
    if valid_emails[0][3] not in ['.com', '.bg', '.org', '.net']:
        raise InvalidDomainError(
            "Domain must be one of the following: .com, .bg, .org, .net")

    print("Email is valid")
    email = input()
