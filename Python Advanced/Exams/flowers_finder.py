from collections import deque

vowels = deque(list(input().split()))
consonants = list(input().split())
rose_word = 'rose'
tulip_word = 'tulip'
lotus_word = 'lotus'
daffodil_word = 'daffodil'
words = ['rose', 'tulip', 'lotus', 'daffodil']
isRose = False
isTulip = False
isLotus = False
isDaffodil = False

while vowels and consonants and not isRose and not isTulip and not isLotus and not isDaffodil:
    vow = vowels.popleft()
    conso = consonants.pop()

    for word in words:
        if word == 'daffodil':
            if vow in word:
                daffodil_word = daffodil_word.replace(vow, '')
            if conso in word:
                daffodil_word = daffodil_word.replace(conso, '')
            if daffodil_word == '':
                isDaffodil = True
                break

        elif word == 'lotus':
            if vow in word:
                lotus_word = lotus_word.replace(vow, '')
            if conso in word:
                lotus_word = lotus_word.replace(conso, '')
            if lotus_word == '':
                isLotus = True
                break
        elif word == 'rose':
            if vow in rose_word:
                rose_word = rose_word.replace(vow, '')
            if conso in rose_word:
                rose_word = rose_word.replace(conso, '')
            if rose_word == '':
                isRose = True
                break
        elif word == 'tulip':
            if vow in word:
                tulip_word = tulip_word.replace(vow, '')
            if conso in word:
                tulip_word = tulip_word.replace(conso, '')
            if tulip_word == '':
                isTulip = True
                break
if isRose:
    print("Word found: rose")
if isTulip:
    print("Word found: tulip")
if isLotus:
    print("Word found: lotus")
if isDaffodil:
    print("Word found: daffodil")
if rose_word != '' and tulip_word != '' and lotus_word != '' and daffodil_word != '':
    print("Cannot find any word!")
if vowels:
    print(f"Vowels left: {' '.join(str(x) for x in vowels)}")
if consonants:
    print(f"Consonants left: {' '.join(str(x) for x in consonants)}")
