def html(title, content, command, comment):

    while 'end of comments' not in command:
        comment.append(command)

        command = input()
    print(f"<h1>\n    {title}\n</h1>")
    print(f"<article>\n    {content}\n</article>")
    for x in comment:
        print(f"<div>\n    {x}\n</div>")


comments = []
html(input(), input(), input(), comments)
