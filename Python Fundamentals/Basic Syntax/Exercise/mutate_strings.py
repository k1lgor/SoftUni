first = input()
second = input()
new = ''
previous = first
for i in range(len(first)):
    for j in range(i + 1):
        new += second[j]
    for k in range(i + 1, len(first)):
        new += first[k]
    if previous != new:
        print(new)
    previous = new
    new = ''
