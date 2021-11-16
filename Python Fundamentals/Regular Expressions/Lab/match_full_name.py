import re

data = input()

occurances = re.findall(r"\b[A-Z][a-z]+ [A-Z][a-z]+\b", data)

print(*occurances)
