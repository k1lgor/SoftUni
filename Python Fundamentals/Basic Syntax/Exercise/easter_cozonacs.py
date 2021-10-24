budget = float(input())
flour_kg = float(input())

egg_pack = flour_kg * 0.75
milk_ltr = flour_kg * 1.25

cozonacs_counter = 0
colored_eggs = 0
milk_250 = milk_ltr / 4
cozonac = flour_kg + egg_pack + milk_250

while budget != 0:
    if budget < cozonac:
        print(
            f'You made {cozonacs_counter} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.')
        break
    budget -= cozonac
    cozonacs_counter += 1
    colored_eggs += 3
    if cozonacs_counter % 3 == 0:
        lost_egg = cozonacs_counter - 2
        colored_eggs -= lost_egg
