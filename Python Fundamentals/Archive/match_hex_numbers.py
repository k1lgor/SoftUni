import re

print(*[i.group() for i in re.finditer(r"\b(0x)?([0-9A-F]{1,})\b", input())])
