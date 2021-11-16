import re

data = input()

dates = re.findall(
    r"\b(?P<day>\d{2})([-.\/])(?P<month>[A-Z][a-z]{2})\2(?P<year>\d{4})\b", data)
for date in dates:
    print(f"Day: {date[0]}, Month: {date[2]}, Year: {date[3]}")
