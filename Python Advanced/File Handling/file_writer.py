def writer():
    with open('my_first_file.txt', 'w') as file:
        file.writelines('I just created my first file!')
    with open('my_first_file.txt', 'r') as file:
        for x in file.readlines():
            print(x)


writer()
