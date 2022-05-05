import os

store = {}


def sorting(store):
    # this is Linux path to desktop
    # will not work for Windows users
    # change it corresponding to your path
    path = '/home/user/Desktop/'
    with open(os.path.join(path, 'report.txt'), 'w') as file:
        for k, v in sorted(store.items(), key=lambda x: x[0]):
            file.write(f".{k}\n")
            for vv in sorted(v):
                file.write(f"- - - {vv}.{k}\n")


def directory(store):
    for x in os.listdir('.'):
        name, ext = x.split('.')
        if ext not in store:
            store[ext] = []
        store[ext].append(name)
    return sorting(store)


directory(store)
