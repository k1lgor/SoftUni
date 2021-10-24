def loadingBar(number):
    bar = '..........'
    replace_index = number // 10
    bar.replace('.', '%', replace_index)
    if number == 100:
        print(f'{number}% Complete!\n[{bar}]')
    else:
        print(f'{number}% [{bar}]\nStill loading...')

loadingBar(number = int(input()))