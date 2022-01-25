def delivery(box, cap):

    racks = 1
    curr_cap = cap
    while box:
        num = box[-1]
        if num <= curr_cap:
            box.pop()
            curr_cap -= num
        else:
            curr_cap = cap
            racks += 1
    print(racks)


box_clothes = [int(x) for x in input().split(' ')]
capacity = int(input())

delivery(box_clothes, capacity)
