l = sorted(map(int, input().split()))
l = list(map(str, l))
new = []
string = ' <= '
counter_string = len(l) - 1
s = ''
for i in l[::]:
    new = list(map(str, i.split()))
    if counter_string == 0:
        s += ''.join(new)
        break
    s += ''.join(new) + string
    counter_string -= 1
print(s)
