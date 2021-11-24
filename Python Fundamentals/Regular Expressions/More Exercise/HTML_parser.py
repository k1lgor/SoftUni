import re

data = input()

title = ' '.join(re.findall(r"<title>(.*)<\/title>", data, re.IGNORECASE))
body = ' '.join(re.findall(r"<body>(.*)<\/body>", data, re.IGNORECASE))

regex_body = re.findall(r"<[a-z\/=\".\s:]+>|\\n", body)

for i in regex_body:
    if i in body:
        body = body.replace(i, "")

print(f"Title: {title}\nContent: {body}")
