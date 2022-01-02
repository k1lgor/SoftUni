def string_exp(data, expl, charr, rslt):

    for i in data:
        if i[0].isdigit():
            expl += int(i[0])
            if expl >= len(i):
                expl -= len(i)
                charr = '>'
            else:
                charr = '>' + ''.join(i[expl:])
                expl = 0
        else:
            charr = i
        rslt.append(charr)
    return rslt


explosion = 0
char = ''
result = []
string_exp(input().split(">"), explosion, char, result)
print(''.join(result))
