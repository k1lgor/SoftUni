num = int(input())
plates = set()

for _ in range(num):
    direction, plate = input().split(', ')
    if direction in 'IN':
        plates.add(plate)
    else:
        plates.discard(plate)
if not plates:
    print("Parking Lot is Empty")
else:
    [print(f"{x}") for x in plates]
