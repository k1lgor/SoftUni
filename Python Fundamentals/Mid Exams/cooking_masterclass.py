from math import floor, ceil

budget, students = float(input()), int(input())
price_flour, price_egg, price_apron = float(input()), float(input()), float(input())
package_flour = students

items = price_apron * ceil(students * 1.2) + price_egg * 10 * students \
        + price_flour * students

fifth_package = floor(package_flour / 5)
items -= fifth_package * price_flour

if items <= budget:
    print(f"Items purchased for {items:.2f}$.")
else:
    print(f"{abs(budget - items):.2f}$ more needed.")