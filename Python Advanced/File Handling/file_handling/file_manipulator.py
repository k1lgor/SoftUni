# name of functions are Linux commands
# I use Arch BTW
import os


def rm_rf(arg):
    if os.path.exists(arg):
        os.remove(arg)
    else:
        print("An error occured")


def sed(arg1, arg2, arg3):
    if not os.path.exists(arg1):
        print("An error occured")
        return
    with open(arg1, 'r+') as file:
        new_file = file.read().replace(arg2, arg3)
        file.seek(0)
        file.truncate()
        file.write(new_file)


def append(arg1, arg2):
    with open(arg1, 'a') as file:
        file.write(f"{arg2}\n")


def touch(arg):
    open(arg, 'w').close()


def manipulator():
    command = input()

    while 'End' not in command:
        command, *args = command.split('-')
        if command == 'Create':
            touch(args[0])
        elif command == 'Add':
            append(args[0], args[1])
        elif command == 'Replace':
            sed(args[0], args[1], args[2])
        elif command == 'Delete':
            rm_rf(args[0])

        command = input()


manipulator()
