def zoo(c, zd):

    while "EndDay" not in c:
        c, token = c.split(": ")

        if c == "Add":
            name, needed_food, area = token.split("-")

            def add(zd):
                if name not in zd:
                    zd[name] = {"food": int(needed_food), "area": area}
                else:
                    zd[name]["food"] += int(needed_food)
                return zd

            add(zd)
        elif c == "Feed":
            name, food = token.split("-")

            def feed(zd):
                if name in zd:
                    zd[name]["food"] -= int(food)
                    if zd[name]["food"] <= 0:
                        print(f"{name} was successfully fed")
                        del zd[name]
                return zd

            feed(zd)
        c = input()


def animals(zd):
    print("Animals:")
    for k, v in sorted(zd.items(), key=lambda x: (-x[1]["food"], x[0])):
        print(f"{k} -> {v['food']}g")


def hungry_animals(zd):
    print("Areas with hungry animals:")
    for k, v in sorted(
        zd.items(), key=lambda x: (-(x[1]["area"]).count(x[1]["area"]), x[1]["area"])
    ):
        print(f"{v['area']}: {v['area'].count(v['area'])}")


command = input()
zoo_dict = {}
zoo(command, zoo_dict)
animals(zoo_dict)
hungry_animals(zoo_dict)
