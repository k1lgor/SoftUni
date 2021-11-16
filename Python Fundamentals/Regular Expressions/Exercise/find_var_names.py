import re

data = input()

var_names = re.findall(r"\b_{1}[a-zA-Z0-9]+\b", data)

print(','.join(x[1:] for x in var_names))
