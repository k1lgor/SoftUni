def extinguish(d, w, f):
    d = d.split("#")
    effort = 0
    total = []
    while w > 0:
        for ff in d:
            type_fire, value = ff.split(" = ")
            if (
                type_fire in f
                and f[type_fire]['Min'] <= int(value) <= f[type_fire]['Max']
                and w >= int(value)
            ):
                w -= int(value)
                effort += int(value) * 0.25
                total.append(int(value))
        break
    print("Cells:")
    for i in total:
        print(f" - {i}")
    print(f"Effort: {effort:.2f}")
    print(f"Total Fire: {sum(total)}")


data = input()
water = int(input())

fire = {
    "High": {"Min": 81,
             "Max": 125},
    "Medium": {"Min": 51,
               "Max": 80},
    "Low": {"Min": 1,
            "Max": 50}
}
extinguish(data, water, fire)
