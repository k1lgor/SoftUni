book = input()
nextbook = ''
counter = 0
while nextbook != 'No More Books':
    nextbook = input()
    if book == nextbook:
        print(f'You checked {counter} books and found it.')
        break
    if nextbook == 'No More Books':
        print(
            f'The book you search is not here!\nYou checked {counter} books.')
    counter += 1
