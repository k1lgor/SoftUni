veg_kg_price = float(input())
fruit_kg_price = float(input())
kg_veg = int(input())
kg_fruit = int(input())

print(f'{(((veg_kg_price * kg_veg) + (fruit_kg_price * kg_fruit)) / 1.94):.2f}')
