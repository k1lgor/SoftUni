import re

data = input()

while 'end' not in data:
    match = re.findall(r"(<a )[a-zA-Z0-9=\"\:\/\.]+(>)[a-zA-Z]+(<\/a>)", data)

    if match:
        for i in match:
            for j in i:
                if j == "<a ":
                    data = data.replace("<a ", "[URL ")
                elif j == ">":
                    data = data.replace(">", "]")
                elif j == "</a>":
                    data = data.replace("</a", "[/URL")

    print(data)
    data = input()
