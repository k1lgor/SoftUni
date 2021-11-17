import re

data = input()

valid = [ele.group() for ele in re.finditer(
    r"\s([a-zA-Z0-9]+[a-zA-Z0-9\.\-\_]*@[a-z]+[a-z\-]*(\.[a-z]+)+)", data)]

print(*valid, sep='\n')
