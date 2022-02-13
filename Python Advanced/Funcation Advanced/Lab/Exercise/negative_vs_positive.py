def func(data):
    positive = sum(filter(lambda x: x > 0, data))
    negative = sum(filter(lambda x: x < 0, data))
    print(f"{negative}\n{positive}")
    if positive > abs(negative):
        print("The positives are stronger than the negatives")
    else:
        print("The negatives are stronger than the positives")


func([int(x) for x in input().split()])
