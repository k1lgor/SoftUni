import re

data = input()

occurances = re.findall("\\b[A-Z][a-z]+ [A-Z][a-z]+\\b", data)
print(' '.join(occurances))
