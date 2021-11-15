title = input()
content = input()
command = input()
comments = []
while 'end of comments' not in command:
    comments.append(command)

    command = input()
print(f"<h1>\n    {title}\n</h1>")
print(f"<article>\n    {content}\n</article>")
for x in comments:
    print(f"<div>\n    {x}\n</div>")
