def diamond(string):

    no_more = False

    while string != []:
        for i in string[::]:
            if string == [] and diamond != 0:
                break
            if i == '>':
                end = string.index(i)
                string = string[end + 1:]
                continue
            diamond = 0
            start = 0
            end = 0
            if i == '<':
                start = string.index(i)
                for j in string[start:]:
                    if j == '>':
                        end = string.index(j)
                        diamond = sum(int(k)
                                      for k in string[start:end] if k.isdigit())
                        print(f'Found {diamond} carat diamond')
                        string = string[end + 1:]
                        break
                break
        if diamond == 0:
            print('Better luck next time')
            break


diamond(list(input()))
