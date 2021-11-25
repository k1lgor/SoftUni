import re

data = input()
locations = re.findall(
    r"(?<=\=)[A-Z][A-Za-z]{2,}(?=\=)|(?<=\/)[A-Z][A-Za-z]{2,}(?=\/)", data)

total = sum((len(loc)) for loc in locations)

print(f"Destinations: {', '.join(locations)}\nTravel Points: {total}")
