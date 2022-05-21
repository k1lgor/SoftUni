import re

number = int(input())

for _ in range(number):
    barcode = re.match(
        r"(@#+)([A-Z][A-Za-z0-9]{4,}[A-Z])(@#+)", input())

    product_group = ''

    if barcode:
        for i in barcode[2]:
            if i.isdigit():
                product_group += i
        if product_group == '':
            product_group = '00'
        print(f"Product group: {product_group}")
    else:
        print("Invalid barcode")
