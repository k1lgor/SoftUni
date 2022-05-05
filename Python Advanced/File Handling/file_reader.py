def reader():
    try:
        with open('numbers.txt') as file:
            result = sum(int(x) for x in file.readlines())
            print(result)
    except FileNotFoundError:
        print("File not found")


reader()
