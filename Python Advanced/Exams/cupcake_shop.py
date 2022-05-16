def stock_availability(box, command, *args):
    if command == 'delivery':
        if args:
            for arg in args:
                box.append(arg)
            return box
    elif command == 'sell':
        if args:
            for arg in args:
                if not str(arg).isalpha():
                    box.reverse()
                    for _ in range(arg):
                        box.pop()
                    box.reverse()
                elif arg.isalpha():
                    if arg in box:
                        while arg in box:
                            box.remove(arg)
        else:
            box.reverse()
            box.pop()
            box.reverse()

        return box


print(stock_availability(
    ["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla",
      "banana"], "delivery", "cookie", "banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(
    ["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(
    ["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))
