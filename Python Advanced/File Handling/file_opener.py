import os


def search_file():

    if os.path.exists('text.txt'):
        print("File found")
    else:
        print("File not found")


search_file()
